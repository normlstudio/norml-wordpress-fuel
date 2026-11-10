# Setup acceptance

Each item requires evidence. Record `verified`, `pending` or `blocked` in the setup file.

- Exact site URL and authorized ownership/scope established.
- All three skills discovered in the chosen local runtime; their source/version is known.
- Hosting connection verifies the actual WordPress root and site URL, not just an SSH login.
- The selected theme/custom source is local, correctly mapped and free of copied secrets.
- Architecture, integrations, design and component documents reflect inspected reality.
- Read-before-change and update-after-change rules are present in the project instructions.
- Existing Git history is preserved; approved remote and clean baseline are verified.
- Preview and test route is usable; errors are not treated as passed checks.
- Publishing policy records environments, checks, approvals and exact release method.
- Database/file backup coverage and private storage are confirmed; restore evidence is recorded.
- An authorized small local/preview change can be inspected and reviewed. Live deployment is
  separate authorization; never mutate a customer's live site merely to prove the package.

If an item is missing, say precisely what is missing. A guide installed successfully does not
prove this particular host or website is ready. No fabricated QA or universal compatibility claim.
