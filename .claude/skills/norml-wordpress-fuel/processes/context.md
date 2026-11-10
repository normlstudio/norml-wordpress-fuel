# Build context for the agent

Use a capable model and the bundled developer skill to inspect the real source and verified
read-only site inventory. Generate evidence-backed Markdown, not generic WordPress advice.

The theme-local `.claude/` contract contains:

- `CLAUDE.md`: a short router to the documents and the read/check/update operating rule.
- `architecture.md`: theme mode, page types, data model and file boundaries.
- `capabilities.md`: verified tools, environments, allowed operations and explicit unknowns.
- `design.md`: measured typography, colors, spacing, layouts and interaction conventions.
- `components.md`: reusable components, source paths, variants, inputs and responsive behavior.
- `ci-cd.md`: the exact preview, QA, approval, publishing and recovery route.
- `docs/integrations.md`: plugins/services, ownership, data direction and observed business rules.
- `fuel-setup.md`: stage status and evidence, without secrets or customer records.

Use existing equivalent files rather than creating competing documentation. Record file paths
and observations. A technical inventory supports the explanation but is not complete architecture
or design documentation. Mark unknowns explicitly and ask only when they block real work.

For every change: read relevant context first; reuse existing components/CSS; verify output
against the documented rules; update affected docs immediately. Preserve decisions that remain
true. The next request must start with the current project, not yesterday's assumptions.

Follow the developer skill’s runtime-entry-point check: verify the selected local agent
loads the shared contract in a fresh session. Codex may need a reference-only AGENTS.md
adapter; do not assume custom global fallback settings or duplicate the canonical rules.
