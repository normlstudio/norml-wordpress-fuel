# WordPress Fuel

A public bundle of three cooperating skills for Claude Code and Codex. Connect your
existing WordPress website, bring its owned source into a local working folder, build
site context, and establish a checked development and publishing workflow.

| Skill | Role |
| --- | --- |
| [WordPress Fuel](.claude/skills/norml-wordpress-fuel/readme.md) | Guides setup and resumes the next incomplete step. |
| [WordPress Connection](.claude/skills/norml-wp-connect/readme.md) | SSH verification, exact site identity and selected source download. |
| [WordPress Copilot Advanced](.claude/skills/norml-wp-developer/readme.md) | Site analysis, durable context, architecture, implementation and QA. |

## Start here

Open Claude Code or Codex in a local project folder. Give it the
[setup guide](https://norml.studio/skills/wordpress-fuel) and ask it to install WordPress
Fuel and help connect your website. Ordinary browser chat and Cowork are not supported
by this terminal-based bundle.

### Claude Code

```sh
npx skills@latest add normlstudio/norml-wordpress-fuel --skill norml-wordpress-fuel norml-wp-connect norml-wp-developer -a claude-code
```

### Codex

```sh
npx skills@latest add normlstudio/norml-wordpress-fuel --skill norml-wordpress-fuel norml-wp-connect norml-wp-developer -a codex
```

Restart/reload the local agent if needed, then ask: “Use WordPress Fuel to connect my
website and continue through source download, site context, Git, publishing and recovery.”
The agent should reuse existing access and ask only for missing details or necessary
provider sign-in/approval. Keep secrets out of chat and Git.

## What happens next

1. Check the existing project and hosting access.
2. Verify SSH host identity and the exact WordPress website.
3. Reuse existing source or download the selected theme/custom plugin into a new folder.
4. Analyze real code and write architecture, components, content and design documentation.
5. Establish Git history, a real preview route, publishing rules and recovery evidence.
6. Make a small scoped change, check the result and keep the documentation current.

Complex sites may need additional work. A local WordPress runtime is useful but not
mandatory when the project has a verified staging preview route. Production data is
not downloaded by default. This package does not guarantee that AI cannot break a site.

## Manual ZIP installation

Extract the complete bundle ZIP into a temporary folder. Its `.claude/skills/` directory
contains all three skill folders. Copy those folders into your project's `.claude/skills/`
for Claude Code or `.agents/skills/` for Codex, preserving any existing customized skills.
Restart/reload the agent and use the first prompt above. The ZIP is a package root with
three skills; do not upload it as a single Cowork skill.

## Existing Advanced installations

The developer component keeps the `norml-wp-developer` slug. This is the v2 Fuel edition;
it replaces generic deploy/sync/scanner helpers with project-owned procedures. Inspect
and preserve customized installed instructions before replacing them. Do not install two
conflicting versions of the same skill. The older standalone repository remains available
for history; it is not modified by this bundle.

## Verification

```sh
python3 -m unittest discover -s tests -v
python3 scripts/validate-package.py
```

Tests cover source capture boundaries and failure behavior using local fixtures. They do
not establish access to a particular customer's host or verify that customer's publishing
and recovery process. Those checks happen during that website's setup.

MIT license. Published by Norml Studio. See [provenance](third-party.md).
