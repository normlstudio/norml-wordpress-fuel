# Guided setup and resumption

Keep `.claude/fuel-setup.md` beside the actual theme code. Use the template in this skill.
Read existing files before writing; merge only the missing setup instructions. Never reset
existing project documentation, Git history, keys, credentials or provider configuration.

1. Confirm the exact website URL, authorized owner and task scope. Discover an existing
   local project/repository before creating another. Identify the active theme, parent theme,
   project-owned plugins and site-critical dependencies through read-only inspection.
2. Use `norml-wp-connect`. Reuse the provider's authenticated API/CLI or SSH. If supported
   automation cannot issue access, stop only that step and ask for the narrow required
   provider consent or credential entry. Never ask for private keys/passwords in chat.
3. Download the relevant source, keeping each source-to-destination mapping. Exclude live
   database, uploads, credentials and backups by default. Preserve existing local work.
4. Pick a preview route with the user. Running WordPress locally is useful but is not
   required merely to read or edit source. A code-only project must have a verified staging
   or equivalent preview and test route before a change can be called checked or released.
   Production data import is a separate, explicitly authorized operation; prefer sanitized
   fixtures or fresh local content. Do not send real customer data to an AI service by default.
5. Inspect and synthesize the site context using the developer skill. Ask for missing
   business rules; never infer a checkout, pricing or integration rule from a filename alone.
6. Adopt GitHub and the site's development/release flow. Use the existing repository when
   present. Verify remote identity without printing credentials embedded in a URL. Stop on
   unrelated work or unexpected remote identity. Record a baseline only after a secret scan.
7. Verify backups and restore instructions before enabling production changes.
8. Run readiness; report what is verified and what remains. On resume, recheck live identity,
   Git state and changed assumptions instead of trusting the old checklist blindly.

The agent owns technical steps. Sign-in, MFA, provider approval and destructive/live decisions
remain with the authorized person. There is no fixed setup-time or hosting-compatibility promise.
