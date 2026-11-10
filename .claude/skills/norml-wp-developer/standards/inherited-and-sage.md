# Inherited themes and Sage

## Inherited projects

Inventory the actual WordPress theme type, active/parent relationship, build tool, package
manager/lockfile, PHP and Node versions, custom plugins, field ownership and integrations.
Read existing instructions and recent history. Trace one real page from route/template to
data, components, assets and browser behavior before changing a shared convention.

Keep working code and its conventions. Prefer a child theme when the current supported
workflow requires it; do not create one mechanically for a custom theme the team owns.
Do not edit WordPress core or third-party plugin/theme source that an update will replace.
For extension work, use existing hooks, a project-owned plugin or the documented child theme.

Identify generated directories from build configuration and Git history. Do not assume
`public/`, `dist/`, `build/` or vendor-like directories are disposable: inherited projects
may keep source or deploy artifacts there. Add ignore rules only after verifying ownership.
Do not overwrite `.gitignore`, agent instructions or deployment configuration during setup.

Record discovered defects separately from the requested change. A full framework migration,
CSS rewrite or data import requires its own scope and recovery plan.

## Sage / Acorn / Blade

When the existing project uses Sage, inspect its actual version and configuration rather than
applying a skeleton from another version. Resolve PHP/Composer, Acorn, Node, Vite/Bud or other
build tooling from the repository. Use its lockfiles and supported runtime versions.

Follow the established responsibilities: WordPress hooks/registering behavior in appropriate
PHP files, view data in the existing composer/controller layer, presentation in Blade views,
shared UI in actual components/partials, and assets through the configured build pipeline.
Use existing ACF registration and field ownership. Do not assume every Sage site uses the
same Tailwind or JavaScript version. Avoid introducing another frontend framework for a
small interaction when the existing stack already supports it.

Do not claim this package installs starter components. Inspect available Blade components
before using them. Keep data normalization out of repeated markup where the existing stack
provides a suitable boundary. Escape by default; review any raw HTML output explicitly.

Run the repository's build and meaningful checks, inspect the resulting asset manifest and
render actual pages. A successful package installation is not a successful theme build.
Theme activation, Acorn cache operations, Composer execution, filesystem permissions and
release commands must follow the verified project contract. Never apply blanket recursive
permissions or activate a theme on production as a discovery step.

## Delivery

Follow `processes/delivery.md`. Identify which build outputs the live runtime needs and how
they reach the host. Preserve environment-specific configuration and customer data.
For direct-production code changes, commit and push the exact result in the same operation.
