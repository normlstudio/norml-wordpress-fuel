import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile
import unittest
from unittest.mock import patch

P = Path(__file__).resolve().parents[1]/'.claude/skills/norml-wp-connect/scripts/site-source.py'
spec=importlib.util.spec_from_file_location('source',P)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class SourceTests(unittest.TestCase):
    def archive(self, root, entries):
        p=root/'source.tar'
        with tarfile.open(p,'w') as t:
            for name,kind in entries:
                i=tarfile.TarInfo(name)
                if kind=='symlink': i.type=tarfile.SYMTYPE;i.linkname='/etc/passwd';t.addfile(i)
                elif kind=='hardlink': i.type=tarfile.LNKTYPE;i.linkname='style.css';t.addfile(i)
                else:
                    body=b'theme source';i.size=len(body);t.addfile(i,io.BytesIO(body))
        return p
    def extraction(self, entries):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d).resolve();out=root/'out';out.mkdir()
            result=m.extract_source(self.archive(root,entries),out)
            return result, sorted(str(p.relative_to(out)) for p in out.rglob('*') if p.is_file())
    def test_clean_capture_excludes_secrets_and_links(self):
        result,files=self.extraction([('style.css','file'),('inc/functions.php','file'),('.env.production','file'),('backup.sql.gz','file'),('linked','symlink')])
        self.assertEqual(files,['inc/functions.php','style.css']);self.assertEqual(result['skipped_entries'],3)
    def test_traversal_and_absolute_rejected(self):
        for name in ['../escape','/etc/passwd','a/../../escape','a\\escape']:
            with self.subTest(name=name),self.assertRaises(ValueError): self.extraction([(name,'file')])
    def test_hardlink_rejected(self):
        with self.assertRaises(ValueError):self.extraction([('style.css','file'),('copy','hardlink')])
    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):self.extraction([('style.css','file'),('style.css','file')])
    def test_existing_and_symlink_destination_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d).resolve();(p/'existing').mkdir();(p/'linked').symlink_to(p/'existing')
            for target in [p/'existing',p/'linked'/'new']:
                with self.assertRaises(ValueError):m.destination_path(target)
    def test_inventory_output_bound(self):
        with self.assertRaises(ValueError): m.inventory_output(['python3','-c','print("x"*1100000)'])
    def test_exact_identity(self):
        data={'url':'https://example.com','root':'/srv/site','content':'/srv/site/wp-content','themes':{'theme':'/srv/site/wp-content/themes/theme'},'plugins':[]}
        with patch.object(m,'inventory_output',return_value=json.dumps(data).encode()):
            self.assertEqual(m.inspect_site('site','/srv/site','https://example.com')['url'],data['url'])
            with self.assertRaises(ValueError):m.inspect_site('site','/srv/site','https://wrong.example')
    def test_connection_validation(self):
        for alias,root in [('-oProxyCommand=bad','/srv/site'),('site','/'),('site','/srv/../site')]:
            with self.assertRaises(ValueError):m.validate_connection(alias,root)
    def test_artifact_boundary(self):
        data={'content':'/srv/site/wp-content','themes':{'theme':'/etc'},'plugins':{}}
        with self.assertRaises(ValueError):m.artifact_path(data,'theme','theme')
        with self.assertRaises(ValueError):m.artifact_path(data,'theme','../theme')
    def test_transport_failure_leaves_no_destination(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d).resolve()/'new'
            with patch.object(m,'ssh_command',return_value=['false']),self.assertRaises(ValueError):
                m.download('site','/srv/site/wp-content/themes/theme',target,'theme')
            self.assertFalse(target.exists());self.assertEqual(list(Path(d).resolve().iterdir()),[])
    def test_successful_transport(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d).resolve();archive=self.archive(root,[('style.css','file'),('functions.php','file')]);target=root/'new'
            with patch.object(m,'ssh_command',return_value=['cat',str(archive)]): result=m.download('site','/srv/theme',target,'theme')
            self.assertEqual(result['files'],2);self.assertTrue((target/'style.css').is_file())
    def test_missing_style_does_not_publish_partial_capture(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d).resolve();archive=self.archive(root,[('functions.php','file')]);target=root/'new'
            with patch.object(m,'ssh_command',return_value=['cat',str(archive)]),self.assertRaises(ValueError):m.download('site','/srv/theme',target,'theme')
            self.assertFalse(target.exists())

if __name__=='__main__':unittest.main()
