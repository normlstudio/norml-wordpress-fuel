# Components and CSS

## Inspect the current system

Before adding a section, find its closest existing equivalent. Inspect markup, styles,
field configuration, JavaScript and responsive states together. Record the real entry
points in `.claude/components.md`; do not invent a component registry from filenames alone.
Identify whether styles are generated, utility-based, SCSS/BEM, block styles or builder-owned.
Keep that architecture. These rules guide additions; they do not authorize a site-wide rewrite.

## Choose the smallest reusable boundary

- A component represents a reusable interface, such as a button, card, media frame or modal.
- A section composes components into a page region with a specific layout and content schema.
- A partial extracts shared rendering without claiming an independent interface.
- A page template composes sections and resolves content; avoid copying component internals.

Document each reusable component's real file, inputs, optional values, variants, states,
content source and known usages. Search usages before changing a shared default.
Keep text, links and media editable through the site's established fields or blocks.
Do not duplicate a whole template for a small visual variation. Introduce a named variant
when its behavior is reusable and its inputs can be expressed clearly.

## Style ownership

In a token-based theme, preserve three layers:

1. Design tokens define actual shared colors, typography, spacing and other design values.
2. Shared components own reusable visual treatment and states.
3. Sections/blocks own local composition and layout.

Do not introduce a page stylesheet that overrides shared component internals throughout
the site. For inherited projects that already use page styles, contain the change and
record the debt; do not rename/reorganize everything during an unrelated feature task.
Use the project's existing utilities or BEM/SCSS conventions. Do not mix a second CSS system
into a working theme without an explicit architectural decision. Keep selectors scoped.
Never edit generated/minified output when the source and build pipeline are available.

## Responsive behavior

Specify what actually changes: column count, order, navigation, media ratio, measure and
spacing. Test the narrowest supported viewport plus representative tablet, desktop and
wide layouts. Check long text, missing media and expanded interaction states.
Avoid fixed heights for variable copy. Use intrinsic layout and sensible wrapping.
Respect reduced motion, visible focus, semantic controls and keyboard operation.

## JavaScript boundaries

Initialize behavior on its owning component; avoid duplicate handlers after dynamic renders.
Use the stack's existing state/event pattern. Clean up listeners and observers when relevant.
Keep interactive states synchronized with accessibility attributes. A modal needs focus
management, Escape behavior and a return target; it is not complete because it opens visually.
No ready-made `x-icon`, `x-picture`, `x-modal` or other component is supplied by this package.
Inspect the project before referencing any such interface.

## Verify a shared change

Render the changed component in each affected context and important variant. Test both
pointer and keyboard behavior. Confirm styles do not leak into neighboring sections.
Update the registry when interfaces, variants or source ownership change.
