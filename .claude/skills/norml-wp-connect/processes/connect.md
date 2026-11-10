# Set up and verify the connection

Ask for the exact site URL and hosting provider only if absent. Reuse an existing authorized
provider connection, configured SSH alias and project setup. Do not reset a working connection.
Inspect provider documentation when capabilities or paths are uncertain.

## Supported provider route

Prefer the provider's supported API, MCP or CLI for the required operation. A connection must
actually expose source access for code development; a content-only endpoint is not a source
checkout. If the provider has no suitable route or SSH is unavailable, state the verified gap.
Do not bypass provider restrictions or promise every hosting plan supports the same process.

## SSH route

The agent checks for OpenSSH, existing agent-managed keys and an appropriate site-scoped user.
Prefer a dedicated unprivileged website user over a server-wide administrator. Generate a
separate key using standard OS tools only when needed, keeping the private key local with
protected permissions and an OS-managed agent/passphrase. Never print or copy the private key.
Only the public key is registered with the host through its supported account tools.

Reuse authenticated provider APIs/CLI for enrollment when available. If only a provider UI can
perform a required action, explain the exact missing capability and obtain browser authorization
or ask for the narrow unavoidable approval. The user completes login/MFA/consent themselves.
Do not ask them to paste secrets into the conversation or create broad credentials unnecessarily.

Verify the server host-key fingerprint using a trusted provider source before adding it to
known_hosts. `ssh-keyscan` alone is not identity verification. Never disable host-key checking.
Configure a descriptive SSH alias in the user's SSH config; do not overwrite unrelated entries.
Store private connection references outside the website repository. Reuse an existing
`norml-wp-developer` machine-local project reference if present; do not create a competing one.

## Read-only verification

Run the helper from this installed skill (resolve its actual path):

```sh
python3 scripts/site-source.py inspect --ssh-alias my-site --wp-root /srv/www/site --expected-url https://example.com
```

Replace the example values with verified project facts; `/srv/www/site` is an example only.
The helper loads WordPress through WP-CLI, compares the actual `home` URL, verifies paths and
returns theme/plugin metadata. A mismatch, missing WP-CLI or inaccessible root is a failure.
Do not claim connected until the intended site has been verified. Record no credential values.

For a new project, SSH config owns the host alias, user, port and key-file reference.
Use one private machine-local mapping at `~/.config/wordpress-fuel/sites/{site-slug}.json`
(mode 0600, parent 0700) containing only `schema_version: 1`, `url`, `ssh_alias`,
`wp_root`, and `local_source`. No passwords, tokens or private keys. Reuse an existing
project registry instead when one already owns this mapping; do not create both.
Keep credentials in the user's existing OS/hosting credential store.

The inventory command makes no intended website writes, but WP-CLI loads site configuration
and may execute must-use plugins or drop-ins even with normal plugins/themes skipped.
Do not run it against a suspected compromised website; use an incident-response process first.
