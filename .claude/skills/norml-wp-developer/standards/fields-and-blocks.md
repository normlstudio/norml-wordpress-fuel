# Structured content and ACF blocks

## Match the current editing model

Inspect registered block types, field groups, local JSON/PHP registrations, templates and
builder data before adding fields. Do not assume ACF exists or install a licensed dependency.
Use the current editor and preserve existing content. Choose custom post types/taxonomies
for repeatable domain records; a collection is not automatically a manually repeated page.

## Schema and rendering

For each new field, document its name, type, required/default behavior, source of truth and
rendering consumer. Use stable field keys in version-controlled definitions when the project
uses ACF local JSON or PHP. Keep group location rules as narrow as the intended editor context.
Avoid conflicting definitions in the database, PHP and JSON. Verify the project's actual
sync/export procedure; do not blindly overwrite a live field group.

Return formats matter: an image may be an ID, array or URL; a relationship may return IDs or
objects. Normalize at the boundary and handle empty/invalid values deliberately. Escape text,
URLs and attributes for their output contexts. Allow rich HTML only through the project's
approved sanitization policy. Check capabilities and nonces for privileged mutations.

## Block composition

Separate field reading/normalization from reusable visual components where the framework
supports it. Keep a block wrapper responsible for its anchor, allowed classes and layout.
Use WordPress block metadata/registration supported by the installed versions. Verify APIs
against the installed ACF/WordPress version before adding version-specific features.

A block's name, for example `acf/example`, is an identifier, not a safe filesystem path.
If resolving a preview asset, map known block identifiers to explicit asset filenames or use
an allowlisted bare slug. Never concatenate untrusted or namespaced block names into paths.
Only display a preview image if that exact asset exists and the editor is in preview mode.
Provide a useful empty state when the editor has not yet supplied fields.

## Compatibility and migration

Changing field names, return formats, repeaters, block names or storage keys can orphan
existing content. Inspect saved examples and explain the migration before changing a schema.
Keep a backup of affected records and a narrow reversible mapping. Test old content as well
as newly entered content. Do not treat a template-only rollback as a database rollback.

## Verification

Check editor insertion, field editing, save/reload and frontend output. Verify empty values,
long copy, large/repeated lists, image alternatives and responsive rendering. Confirm the
content owner can edit the new content without changing PHP or hardcoded markup.
