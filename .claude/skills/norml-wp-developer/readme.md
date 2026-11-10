# WordPress Copilot Advanced

Map an existing WordPress website, maintain its context and implement checked changes within its current architecture.

Part of the WordPress Fuel bundle. Use Claude Code or Codex in a local project folder.

## Install

See [installation](install.md). Install the full bundle for first-time website setup.

## How it works

1. **Inspect.** Read the actual theme, components, data and delivery rules.
2. **Document.** Build evidence-backed site context and record unknowns.
3. **Implement.** Reuse the existing stack and component conventions.
4. **Verify.** Check the rendered result and follow the project release contract.

## What you need

An authorized website, access to its hosting account and a local agent with filesystem,
terminal and Git access. Hosting must support SSH; the source inspection helper also
needs remote WP-CLI and tar. The agent reports provider-specific missing access instead
of claiming every host is supported. Node.js 22 or newer and npm is needed for the install command.

## Boundaries

This is a guided workflow. It does not supply a universal deployment pipeline, guarantee
error-free AI output, or make a complex legacy website understandable without inspection.
Do not paste credentials into chat. Production database imports are not part of the default
source download. Establish a real preview, release and recovery route before publishing.

## Package

Read [the agent entry point](SKILL.md) for the operating contract and linked procedures.
[Changes](changelog.md) records the package version and migration differences.

Covers SKILL.md v2.0.0. Generated 2026-11-10.
