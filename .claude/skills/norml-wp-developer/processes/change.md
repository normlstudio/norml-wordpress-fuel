# Make a scoped change

Read the relevant project context and inspect current Git state. Preserve unrelated changes.
Clarify the desired behavior only where the source is genuinely ambiguous. Identify affected
components and data ownership before editing. Propose the WordPress primitive when architecture
is needed; do not hide a new data model inside a page or theme template.

Reuse the existing component, template and CSS system. Keep domain functionality in a suitable
plugin or established application layer; theme presentation stays in the theme. Match the site's
stack and conventions. Do not add dependencies or reorganize unrelated code for a small task.

Implement the smallest complete change. Run relevant syntax/build checks and meaningful tests.
Open the rendered result in the approved preview and verify the requested interaction, responsive
states and affected business flow. Screenshots can communicate a visual bug; they do not replace
functional verification. Report failures; do not suppress them to produce a success message.

Update affected architecture, component, design, integration and delivery documents. Preserve
still-valid decisions. Record the code change through the existing Git workflow. If publishing
was authorized, follow delivery; otherwise leave a checked local/preview result for review.
The user directs the business outcome and checks the result; complex work can still need a developer.
