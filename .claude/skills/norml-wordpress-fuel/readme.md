# WordPress Fuel

Guide your local AI agent through connecting an existing WordPress website, downloading its source and establishing a documented development workflow.

Part of the WordPress Fuel bundle. Use Claude Code or Codex in a local project folder.

## Install

See [installation](install.md). Install the full bundle for first-time website setup.

## How it works

1. **Prepare.** Inspect your project and reuse existing setup.
2. **Connect.** Verify SSH and the exact WordPress site.
3. **Understand.** Download selected source and document the website.
4. **Work.** Establish Git, publishing and recovery; then make a checked change.

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

Covers SKILL.md v1.0.1. Generated 2026-11-10.

Setup checks that the selected agent actually loads the shared site instructions on future requests. Existing instruction files are preserved.
