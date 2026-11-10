# Install WordPress Fuel

Use a local Claude Code or Codex project. Node.js 20+ runs the skills installer;
Python 3, Git and OpenSSH support the included helpers. The agent checks and uses
supported installation methods for missing tools, explaining any necessary system change.
macOS and Linux shell workflows are the documented path. Native Windows is not advertised.

Run from the local website project. These commands select exactly the three bundled skills:

```sh
npx skills@latest add normlstudio/norml-wordpress-fuel --skill norml-wordpress-fuel norml-wp-connect norml-wp-developer -a claude-code
```

```sh
npx skills@latest add normlstudio/norml-wordpress-fuel --skill norml-wordpress-fuel norml-wp-connect norml-wp-developer -a codex
```

Use the command for your runtime, then start or reload its project session and ask:

> Use WordPress Fuel to connect my existing WordPress website and complete the six setup stages.

The website has a copyable prompt at https://norml.studio/skills/wordpress-fuel.
Ask the agent to read it, install the bundle for the current runtime and continue setup.
Verify all three exact skill names and supporting files through runtime discovery before use.
Do not advertise a plain ChatGPT conversation or Cowork as this local coding environment.

## Existing installations

Before installation, inspect the runtime's existing skills. If `norml-wp-developer` is
already installed from the standalone Advanced package or has local changes, preserve that
exact installation and explain the version difference before a user-approved replacement.
Do not merge two versions or silently overwrite customized rules. A project-scoped install
can isolate this bundle from unrelated projects; verify which version the runtime loads.

## Download

The release ZIP contains the repository root and `.claude/skills/` with all three skills.
Extract it into a temporary directory and use the supported skills CLI local-source install
for the current runtime, or follow that runtime's documented project-skill installation.
Verify discovery; copying a folder alone is not proof the runtime can use it.
