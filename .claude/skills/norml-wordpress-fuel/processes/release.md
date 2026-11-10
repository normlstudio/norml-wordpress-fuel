# Define how the website is updated

Connection grants access; it does not grant permission to publish. Document the site's exact
process in `.claude/ci-cd.md`, using an existing equivalent file if one already owns this policy.

Record the local working scope, preview environment, test commands, code review, approval
boundary, deployment command/provider pipeline, released revision and public verification.
For a team workflow, preserve branches, pull requests, QA and staging. Do not invent a simpler
route just because the agent can access production.

A direct-production route may be explicitly allowed for a bounded task type. Name the scope,
checks and rollback requirements. It must never be inferred from convenience or past access.
The agent verifies the target and exact release revision immediately before a live action.

Use an existing reviewed pipeline. This bundle deliberately ships no generic file-deletion
or database-overwrite deployment helper. If a project lacks a deploy process, prepare the
provider-specific implementation and verification before proposing a production release.
Never run a broad `rsync --delete`, mirror a local database over live orders, or turn a failed
build/test/transfer into success. Exit on failures and preserve the error as a blocked stage.

After an authorized release, verify the affected public behavior and record the exact source
revision and result. If verification fails, follow the documented recovery procedure; do not
keep applying speculative live changes.

Every authorized production code write, including direct-production exceptions, requires
the exact change to be committed and pushed to the configured Git remote in the same operation.
Stage only the task's files. If commit or push fails, report the live/source mismatch and resolve
it before calling delivery complete; never silently leave production ahead of Git.
