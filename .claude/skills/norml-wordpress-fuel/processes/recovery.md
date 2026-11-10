# Verify a route back

Git is code history. The database and uploaded files have separate recovery needs.

Inspect the host's actual backup configuration through its supported tools: coverage, schedule,
retention, storage location, access policy and restore method. Prefer existing host-level daily
backups. If missing, prepare the host-supported setup and obtain the necessary configuration
approval. Do not claim this bundle automatically creates backups on every provider.

Backup files must not live in a publicly downloadable web directory. Keep secrets and customer
data out of project docs, repositories and chat. Record references and coverage, not backup contents.

Verify recovery through an authorized isolated restore test or valid recent provider/site evidence;
record what was actually tested and what was only documented. A test must not overwrite live data.
Confirm that media/files are covered as well as the database where required.

Before a rollback: identify the affected code/data, checkpoint, new orders/content since it, and
how those records will be preserved or reconciled. A database restore can erase newer transactions.
Explain this exact impact and get explicit authorization before a destructive restore. If a safe
recovery path cannot be established, keep production changes blocked and continue local work.
