# Change acceptance

- Intended behavior and affected scope are understood.
- Current architecture and existing components were used.
- Relevant lint, syntax/build and meaningful tests passed; failures are listed honestly.
- The rendered page and affected interaction were inspected in an approved preview.
- Relevant responsive, accessibility, security and integration behavior was checked.
- Unrelated work, live orders, credentials and third-party ownership were preserved.
- Affected context files were updated and source history is coherent.
- Any authorized release used the documented route and its exact revision was verified live.
- Remaining uncertainty or a required developer handoff is explicit.

Do not invent universal test commands. Resolve them from the real project. No test is permission
for live orders, payments, customer emails or other external effects.
