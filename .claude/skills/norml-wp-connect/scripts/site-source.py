#!/usr/bin/env python3
"""Read-only WordPress identity inspection and scoped source capture. Python 3.9+."""
import argparse
import fnmatch
import json
import os
from pathlib import Path, PurePosixPath
import re
import shlex
import shutil
import subprocess
import sys
import tarfile
import tempfile
from urllib.parse import urlsplit

MAX_ARCHIVE = 512 * 1024 * 1024
MAX_FILES = 30000
EXCLUDED = ('.git', '.env*', 'wp-config*', '*.pem', '*.key', '*.p12', '*.pfx',
            '*.sql', '*.sql.*', '*.sqlite*', '*.zip', '*.tar', '*.tar.*', '*.tgz',
            '*.log', '.DS_Store', 'node_modules', 'vendor', 'uploads', 'backups',
            'backup', '.ssh', '.aws', '*credentials*', '*secrets*')
PHP = r"""$themes = []; foreach(wp_get_themes() as $slug=>$theme) {
$themes[$slug] = realpath($theme->get_stylesheet_directory()); }
require_once ABSPATH.'wp-admin/includes/plugin.php'; $plugins=[];
foreach(get_plugins() as $file=>$data) { if(strpos($file,'/') !== false) {
$slug=explode('/',$file)[0]; $plugins[$slug]=realpath(WP_PLUGIN_DIR.'/'.$slug); }}
echo json_encode(['url'=>home_url(), 'root'=>realpath(ABSPATH),
'content'=>realpath(WP_CONTENT_DIR), 'active_theme'=>get_stylesheet(),
'parent_theme'=>get_template(), 'themes'=>$themes, 'plugins'=>$plugins]);"""


def normalized_url(value):
    u = urlsplit(value)
    if u.scheme not in ('http', 'https') or not u.hostname or u.username or u.password or u.query or u.fragment:
        raise ValueError('Expected a public HTTP(S) website URL without credentials, query or fragment')
    return (u.scheme.lower(), u.hostname.lower(), u.port, u.path.rstrip('/'))


def validate_connection(alias, root):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', alias):
        raise ValueError('Use an existing SSH config alias, not a host option or command')
    if not root.startswith('/') or root == '/' or '..' in PurePosixPath(root).parts or any(ord(c)<32 for c in root):
        raise ValueError('A specific absolute WordPress root is required')


def ssh_command(alias, command):
    return ['ssh', '-o', 'BatchMode=yes', '-o', 'StrictHostKeyChecking=yes',
            '-o', 'ConnectTimeout=15', alias, command]


def inventory_output(command):
    import time
    with tempfile.TemporaryFile() as output, tempfile.TemporaryFile() as errors:
        process = subprocess.Popen(command, stdout=output, stderr=errors)
        started = time.monotonic()
        try:
            while process.poll() is None:
                if time.monotonic()-started > 60 or os.fstat(output.fileno()).st_size > 1048576:
                    raise ValueError('WordPress inventory exceeded time/output limit')
                time.sleep(0.1)
            if process.returncode or os.fstat(output.fileno()).st_size > 1048576:
                raise ValueError('WordPress inventory failed or exceeded output limit')
            output.seek(0)
            return output.read(1048576)
        finally:
            if process.poll() is None:
                process.kill()
            process.wait()


def inspect_site(alias, root, expected_url):
    validate_connection(alias, root)
    expected = normalized_url(expected_url)
    command = 'wp --path=' + shlex.quote(root) + ' --skip-plugins --skip-themes eval ' + shlex.quote(PHP)
    output = inventory_output(ssh_command(alias, command))
    try:
        info = json.loads(output)
        if normalized_url(info['url']) != expected:
            raise ValueError('Remote website URL does not match the expected website')
        for key in ('root', 'content'):
            if not isinstance(info[key], str) or not info[key].startswith('/') or info[key]=='/':
                raise ValueError('Invalid WordPress path returned')
        if not isinstance(info['themes'], dict) or not isinstance(info['plugins'], (dict, list)):
            raise ValueError('Invalid source inventory')
        return info
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        raise ValueError('WordPress returned an invalid identity response') from exc


def artifact_path(info, kind, slug):
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', slug):
        raise ValueError('Invalid source slug')
    source = info['themes' if kind == 'theme' else 'plugins']
    source = source.get(slug) if isinstance(source, dict) else None
    content = PurePosixPath(info['content'])
    if not source or '..' in PurePosixPath(source).parts or content not in PurePosixPath(source).parents:
        raise ValueError('Artifact is not a registered directory inside the verified content root')
    return source


def destination_path(value):
    raw = Path(value).absolute()
    if '..' in raw.parts or raw.exists() or raw.is_symlink():
        raise ValueError('Destination must be a new path without traversal')
    if not raw.parent.is_dir() or any(p.is_symlink() for p in [raw.parent, *raw.parents]):
        raise ValueError('Destination parent must exist and have no symlink components')
    return raw


def excluded(name):
    return any(fnmatch.fnmatch(part.lower(), pattern.lower()) for part in name.parts for pattern in EXCLUDED)


def extract_source(archive, target):
    total = 0
    files = 0
    skipped = 0
    seen = set()
    with tarfile.open(archive, 'r:*') as tar:
        for count, member in enumerate(tar, 1):
            if count > MAX_FILES:
                raise ValueError('Archive exceeds entry limit')
            name = PurePosixPath(member.name)
            if name.is_absolute() or '..' in name.parts or '\\' in member.name or any(ord(c)<32 for c in member.name):
                raise ValueError('Unsafe archive path')
            if str(name) == '.':
                continue
            if excluded(name) or member.issym():
                skipped += 1
                continue
            if not (member.isdir() or member.isfile()):
                raise ValueError('Archive contains a hard link or special file')
            out = target.joinpath(*name.parts)
            if str(name) in seen:
                raise ValueError('Duplicate archive path')
            seen.add(str(name))
            if member.isdir():
                out.mkdir(parents=True, exist_ok=True, mode=0o700)
                continue
            total += member.size
            if total > MAX_ARCHIVE:
                raise ValueError('Expanded source exceeds size limit')
            out.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            with tar.extractfile(member) as src, out.open('xb') as dst:
                shutil.copyfileobj(src, dst)
            out.chmod(0o700 if member.mode & 0o111 else 0o600)
            files += 1
    if files == 0:
        raise ValueError('No source files found')
    return {'files': files, 'bytes': total, 'skipped_entries': skipped}


def download(alias, source, destination, kind):
    target = destination_path(destination)
    # Only a new local directory is written. There are no remote write commands.
    with tempfile.TemporaryDirectory(prefix='.fuel-source-', dir=target.parent) as tmp:
        tmp = Path(tmp)
        archive = tmp/'source.tar'
        command = 'tar -C ' + shlex.quote(source) + ' -cf -'
        for pattern in EXCLUDED:
            command += ' --exclude=' + shlex.quote(pattern)
        command += ' .'
        # File-backed stdout prevents binary output or source contents entering the chat.
        with archive.open('xb') as stream, tempfile.TemporaryFile() as errors:
            process = subprocess.Popen(ssh_command(alias, command), stdout=stream, stderr=errors)
            import time
            started = time.monotonic()
            try:
                while process.poll() is None:
                    if time.monotonic()-started > 120 or archive.stat().st_size > MAX_ARCHIVE:
                        raise ValueError('Source transfer exceeded time/size limit')
                    time.sleep(0.1)
                if process.returncode or archive.stat().st_size > MAX_ARCHIVE:
                    raise ValueError('Source transfer failed or exceeded size limit')
            finally:
                if process.poll() is None:
                    process.kill()
                process.wait()
        extracted = tmp/'files'
        extracted.mkdir(mode=0o700)
        stats = extract_source(archive, extracted)
        if kind == 'theme' and not (extracted/'style.css').is_file():
            raise ValueError('Registered theme capture has no style.css')
        # Recheck immediately before rename. Never replace a pre-existing target.
        destination_path(target)
        if sys.platform == 'darwin':
            import ctypes
            libc = ctypes.CDLL(None, use_errno=True)
            if libc.renamex_np(os.fsencode(extracted), os.fsencode(target), 0x00000004):
                raise OSError(ctypes.get_errno(), 'Exclusive destination rename failed')
        else:
            # Reserve the destination exclusively, then move owned entries into it.
            target.mkdir(mode=0o700)
            try:
                for child in extracted.iterdir():
                    child.rename(target/child.name)
            except BaseException:
                shutil.rmtree(target)
                raise
        return stats


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['inspect', 'download'])
    parser.add_argument('--ssh-alias', required=True)
    parser.add_argument('--wp-root', required=True)
    parser.add_argument('--expected-url', required=True)
    parser.add_argument('--kind', choices=['theme', 'plugin'])
    parser.add_argument('--slug')
    parser.add_argument('--destination')
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    try:
        info = inspect_site(args.ssh_alias, args.wp_root, args.expected_url)
        if args.action == 'inspect':
            print(json.dumps(info, indent=2))
            return
        if not all([args.kind, args.slug, args.destination]):
            raise ValueError('Download requires kind, slug and destination')
        source = artifact_path(info, args.kind, args.slug)
        target = destination_path(args.destination)
        result = {'website': info['url'], 'source': source, 'destination': str(target), 'applied': False}
        if args.apply:
            result.update(download(args.ssh_alias, source, target, args.kind))
            result['applied'] = True
        print(json.dumps(result, indent=2))
    except (ValueError, OSError, subprocess.TimeoutExpired, tarfile.TarError) as exc:
        # Exception messages from remote processes/archive contents are not printed.
        print('Source check/capture failed: ' + (str(exc) if isinstance(exc, ValueError) else type(exc).__name__), file=sys.stderr)
        raise SystemExit(1)

if __name__ == '__main__':
    main()
