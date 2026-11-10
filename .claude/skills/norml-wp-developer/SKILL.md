---
name: norml-wp-developer
version: 2.0.0
description: >
  WordPress Copilot Advanced, Fuel edition: inspect an existing WordPress theme and project-owned plugins, build and maintain architecture/design/component context, implement scoped changes, verify them and follow the project’s Git, release and recovery contract. Supports inherited themes and Sage without forcing a migration.
license: MIT
---

# WordPress Copilot Advanced — Fuel edition

This is the developer component of WordPress Fuel. It retains the architecture-first,
existing-stack, QA and Git workflow from WordPress Copilot Advanced, with a reviewed
portable setup and explicit project-owned publishing. Version 2 does not ship the old
generic deploy/sync/scanner executables. See [changelog](changelog.md).

## Entry and boundaries

For first connection or source download use bundled `norml-wordpress-fuel` and
`norml-wp-connect`. Begin here once the selected source is available locally and mapped to
its verified website. Work in the real theme root, with explicit paths to any owned plugins.
Claude Code and Codex are the supported local agent surfaces. No Cowork or web-chat promise.

Read existing instructions, Git status, architecture and delivery rules before editing.
Preserve the current framework, page builder, data model and team's process. Do not turn
an inherited theme into Sage or replace a working store simply because another stack is familiar.

## Understand the website

Follow [site context](processes/site-context.md). Inspect actual files and verified site
inventory, then create or update organized Markdown with evidence and explicit unknowns.
Use a capable model for the initial analysis. The agent writes the documentation; the user
supplies missing business rules and approves meaningful behavior changes.

## Implement and verify

Follow [change](processes/change.md), [WordPress standards](standards/wordpress.md), and
[QA](qa/change-checks.md). Reuse components, CSS, content structure and existing conventions.
Load [components and CSS](standards/components-and-css.md) for interface work,
[fields and blocks](standards/fields-and-blocks.md) for structured content, and
[inherited themes and Sage](standards/inherited-and-sage.md) for stack-specific decisions.
For a new repeatable data type, choose the appropriate WordPress primitive before building.
Read context before each task and update it after changing architecture, design or behavior.

## Git, publishing and recovery

Follow [delivery](processes/delivery.md). Existing source history and the site's documented
pipeline win. Verify remote identity, tests and exact revision before an authorized release.
No generic destructive deploy helper is included. A new pipeline must be prepared and checked
for this project before it is used. Database restore and live content mutation need their own
explicit authorization and current backup/recovery evidence.

## Success

A task is complete when the requested behavior is implemented, the actual result is checked,
affected documentation is current, source changes are recorded as the project requires,
and any authorized release is verified. Clearly report blockers and unverified behavior.
A generated file, successful SSH command or passing syntax check alone is not completion.
