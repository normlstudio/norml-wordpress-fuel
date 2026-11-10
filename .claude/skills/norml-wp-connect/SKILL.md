---
name: norml-wp-connect
version: 1.0.0
description: >
  Guide secure hosting and SSH access for an existing WordPress site, verify its actual URL/root, and download selected theme or custom-plugin source without live mutations or customer data. Prepare a local project for WordPress Fuel and the bundled developer skill.
license: MIT
---

# WordPress connection and source download

This bundled skill connects an authorized website to the local workspace. It verifies identity
before reading source and never treats a successful SSH login as proof of the correct site.

## Flow

1. Read [connection setup](processes/connect.md). Resolve site URL, provider and existing access.
2. Verify a supported provider route. For SSH/WP-CLI use the read-only helper described there.
3. Read [source download](processes/download-source.md). Download only selected owned code into
   a new local destination. Existing local work and all production data remain intact.
4. Hand the verified theme-root project and source mappings to `norml-wp-developer`; return
   evidence to `norml-wordpress-fuel`. No parallel `.claude/fuel/site.json` contract is created.

## Tools and boundaries

The helper requires Python 3, OpenSSH and remote WP-CLI/tar. It uses a configured SSH alias,
strict host-key checking and batch authentication. It cannot enroll hosting keys or grant itself
access; provider setup is agent-guided through official supported tools.

Only `inspect` and `download` operations exist. Download plans by default; `--apply` writes a
new local folder after identity verification. There is no upload, delete, database export,
production deploy or credential-print operation. No secret values belong in arguments or chat.

Read [security](standards/security.md) before connecting. Unsupported providers or insufficient
permissions block that step; never bypass them or silently take over a browser session.
