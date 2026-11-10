# WordPress development standards

## Existing architecture first

Identify Sage/Acorn/Blade, a classic theme, block theme or inherited framework before changing it.
Follow its actual build system and data conventions. Do not impose a migration as part of setup.
Reuse existing design tokens, components, templates and field structures.

## Data model and placement

Use posts/pages for their intended content, custom post types for repeatable domain records,
taxonomies for classification, and structured fields for explicit data. Explain archive/single
routes and permalink implications before introducing them. Put site-wide domain functionality
in a suitable plugin; keep theme presentation separate. Preserve integrations and field ownership.

## Secure implementation

Check capabilities at privileged entry points; nonces do not replace authorization. Validate
and sanitize input for its type, escape output for its context and use prepared database queries.
Do not expose credentials or customer records in JavaScript, logs or errors. Respect WordPress
APIs and hooks. Avoid edits to core or third-party plugin files that updates will overwrite.

## Components and responsive behavior

Reuse site components and CSS. Document inputs, variants, states, responsive rules and accessibility.
Keep keyboard interaction, labels, focus and contrast usable. Test actual rendering and interactions.
When the project uses a separate design/anti-pattern contract, follow it.

## Testing and boundaries

Use relevant project checks and meaningful regression coverage. Payment/order/email tests must
not create real external effects without explicit authorization. Local/staging data should be
sanitized. Do not install arbitrary plugins or send site content to external services merely to
speed up the task. Public documentation can inform implementation; verify current API behavior
where version-specific accuracy matters.
