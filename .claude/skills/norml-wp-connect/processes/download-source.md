# Download the existing owned source

Inspect before copying. Identify the active theme, parent theme if any, and project-owned
plugins. Preserve licensed dependencies and do not redistribute a customer's code.
Use the existing local repository when it already contains this source; do not create a fork
or replace local changes. Compare remote and local identities before choosing a source.

For a new working copy, the helper plans the exact selected artifact:

```sh
python3 scripts/site-source.py download --ssh-alias my-site --wp-root /srv/www/site --expected-url https://example.com --kind theme --slug my-theme --destination /local/projects/my-theme
```

Review the verified source and destination, then add `--apply` for the authorized local copy.
The destination must not exist, its parent must exist, and neither may traverse a symlink.
The helper retrieves only that registered theme/plugin's files, rejects unsafe archive paths
and special files, skips symlinks, excludes common credential/backup files and never uploads.
For a selected custom plugin, use `--kind plugin --slug my-plugin`. Single-file plugins require
manual source review and are not downloaded by this directory-only helper.

Do not bulk-download all plugins, uploads or the database. A local running site can use fresh
or sanitized content. Any real production-data import needs separate specific authorization
and private handling. Theme source itself may contain hardcoded secrets: inspect locally for
secret patterns before Git or model ingestion, report locations only, and fix exposure through
the site's approved credential process. Exclusion patterns are not a guarantee of secret-free code.

Record the exact source-to-local mapping, active/parent theme and custom-plugin dependencies.
Keep assets needed by the code; flag skipped symlinks or missing dependencies. Do not call the
site fully runnable merely because files downloaded. Hand off context building to the developer
skill and select a real preview route before implementing or publishing a change.
