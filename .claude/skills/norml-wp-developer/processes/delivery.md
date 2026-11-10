# Follow the project’s delivery contract

Read `.claude/ci-cd.md` or its established equivalent before changing live state. It must name
the working scope, preview target, required checks, approval, deployment process and recovery.
If it is missing, prepare it with Fuel before any live action.

Adopt the existing Git repository. Inspect a remote safely: parse it and reject credential-bearing
URLs; never print embedded passwords/tokens. Verify the intended provider, owner and repository.
Commit only the task's intended source changes, with a meaningful rationale; do not sweep up
unrelated work. Keep secrets, database dumps, uploads and backup artifacts outside Git.

Use the team’s branches, pull requests, CI and staging where that is its process. A direct-production
exception must already define the allowed task type and checks. Access alone is not approval.
Before release, verify the exact target, tested revision, uncommitted state, approval and recovery
checkpoint. Use the existing reviewed deploy pipeline; never invent a broad file mirror or database
replacement. Treat failed build, upload, smoke check or health check as failure and stop.

Verify the affected public behavior after release and record source/release parity. A code rollback
uses the relevant revision; database/file recovery uses the separately verified private backup.
Do not overwrite newer orders or content without a specific preservation plan and authorization.

Every authorized production code write, including direct-production exceptions, requires
the exact change to be committed and pushed to the configured Git remote in the same operation.
Stage only the task's files. If commit or push fails, report the live/source mismatch and resolve
it before calling delivery complete; never silently leave production ahead of Git.
