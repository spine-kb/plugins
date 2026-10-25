# Move to the Spine plugin

The source is [spine-kb/plugins](https://github.com/spine-kb/plugins). OpenAI
and Claude retain separate catalogs, both identified as `spine-kb`. OpenAI shows
**SpineKb** in its marketplace picker. All three adapters now use the plugin
name `spine`; provider suffixes remain only in their source directories.

| Client      | Previous plugin identities                                | Current plugin identity |
| ----------- | --------------------------------------------------------- | ----------------------- |
| OpenAI      | `spine-openai@spine-kb`, `spine-openai@spine-team-openai` | `spine@spine-kb`        |
| Claude      | `spine-claude@spine-kb`, `spine-claude@spine-team-claude` | `spine@spine-kb`        |
| Antigravity | `spine-antigravity`                                       | `spine`                 |

The renamed package is a new plugin identity. There is no automatic migration or
legacy alias in these catalogs. Remove the old package and install the new one
in your client. If you already use the `spine-kb` marketplace, keep it and
refresh its source. Only installations using an older `spine-team-*` catalog
need to replace that catalog. A repository redirect alone does not migrate
registered marketplaces or installed plugins.

## OpenAI local clients

Remove the old `spine-openai` plugin using your client's plugin controls. If you
already registered `spine-kb`, refresh it:

```sh
codex plugin marketplace upgrade spine-kb
```

If `codex plugin marketplace list` instead shows `spine-team-openai`, remove
that old catalog:

```sh
codex plugin marketplace remove spine-team-openai
```

Register the current marketplace if it is not already listed:

```sh
codex plugin marketplace add spine-kb/plugins
```

Install **Spine** from **SpineKb** in the desktop app and authenticate if
prompted. Update project settings keyed by either old OpenAI identity in the
table to `spine@spine-kb`. Start a new conversation and check the Spine mention
and a private document link copied from the current app. A marketplace refresh
alone does not install the renamed package or verify its displayed name.
[OpenAI marketplace commands](https://developers.openai.com/plugins/build/plugins).

## Claude

For a plugin installed through Claude web/desktop, use **Customize → Plugins**
to remove the old Spine installation. If the marketplace is already `spine-kb`,
keep it and use **Check for updates** in its marketplace controls. If you still
use `spine-team-claude`, replace that old marketplace with
`https://github.com/spine-kb/plugins`. Install Spine and connect it through its
**Connectors** tab.

For a local Claude Code installation, remove the old `spine-claude` plugin
through the client's plugin management. Keep and refresh an existing `spine-kb`
marketplace. Remove the old catalog only if `claude plugin marketplace list`
lists `spine-team-claude`:

```sh
claude plugin marketplace remove spine-team-claude
```

Removing a Claude Code marketplace also uninstalls its plugins and removes saved
plugin data and settings. Review any data you need before removing it. Register
the current marketplace only if it is not already listed:

```sh
claude plugin marketplace add spine-kb/plugins
```

Install the renamed package:

```sh
claude plugin install spine@spine-kb
```

Update any project references keyed by either old Claude identity in the table
to `spine@spine-kb`, authenticate if prompted, and start a new session.
[Claude Code migration commands](https://code.claude.com/docs/en/plugins/cli-reference).

## Antigravity and repository clones

Remove the old `spine-antigravity` installation using the client's plugin
management before installing the renamed adapter. For an existing clone, update
its remote if needed and pull the current packages:

```sh
git remote set-url origin https://github.com/spine-kb/plugins.git
git pull --ff-only
agy plugin install ./plugins/spine-antigravity
```

Run these commands from the clone's root. The directory keeps its provider
suffix; the installed plugin identity is now `spine`. New clones can follow the
[README](../README.md#antigravity-cli). Client migration behavior remains
unverified; see [verification](verification.md).

## New production connection

The production MCP endpoint is `https://app.spine-kb.com/mcp`. The former
`spine.pavorik.com` deployment and its connections are not preserved. Create or
update your client connection to the new endpoint and complete OAuth with your
current Spine account; installing the updated files does not authorize it. Copy
new document links from the app instead of rewriting an old host or path.

After reconnecting, check a known document in a new chat. Full installation,
OAuth, bootstrap delivery, and mobile behavior still need client-specific
verification against this production app; see [verification](verification.md).
