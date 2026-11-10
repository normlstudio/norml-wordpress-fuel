# Inspect and explain the real site

1. Read existing project instructions and inspect source ownership: active/parent theme,
   custom plugins, must-use plugins, build tooling, dependencies and repository boundaries.
2. Map WordPress data primitives: post types, taxonomies, archives/singles, permalink rules,
   ACF/other field ownership, reusable blocks and page templates. Do not infer live values
   from stale exports. Use read-only WP-CLI or the site's supported API where authorized.
3. Map integrations: what calls what, which system owns each field, jobs/webhooks, business
   rules and failure paths. Customer/order samples require private, minimized handling.
4. Inspect templates and CSS plus actual rendered pages in the agreed preview. Document
   measured design tokens, component source paths, variants, field inputs and responsive states.
5. Record environment/tool capabilities, project tests and the current release/recovery route.
6. Synthesize the context files described by Fuel, adopting existing equivalents. Link the
   short project router to detailed docs. Evidence paths support conclusions; unknowns stay unknown.

Use `templates/project-instructions.md` as an additive starting point, never overwrite an
existing instruction file. Documentation is for the next agent as well as the current one:
concise rules, real source paths and the reasons behind important site-specific choices.
Keep credentials, private connection material and live customer records outside committed docs.
