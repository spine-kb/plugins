# Move to SpineKb marketplaces

The source is now [spine-kb/plugins](https://github.com/spine-kb/plugins).
OpenAI and Claude retain separate catalogs, both identified as `spine-kb`.
OpenAI shows **SpineKb** in its marketplace picker. Package names stay the same.

| Client | Previous plugin identity         | Current plugin identity |
| ------ | -------------------------------- | ----------------------- |
| OpenAI | `spine-openai@spine-team-openai` | `spine-openai@spine-kb` |
| Claude | `spine-claude@spine-team-claude` | `spine-claude@spine-kb` |

A repository redirect does not migrate a registered marketplace or installed
plugin to its new ID. There is no automatic migration or legacy alias in these
catalogs. Update the source and reinstall the package in your client.

## OpenAI local clients

Remove the old Spine plugin using your client's plugin controls. If
`codex plugin marketplace list` still shows the old catalog, replace it:

```sh
codex plugin marketplace remove spine-team-openai
codex plugin marketplace add spine-kb/plugins
```

Install **Spine** from **SpineKb** in the desktop app and authenticate. If you
have project settings for `spine-openai@spine-team-openai`, update their key to
`spine-openai@spine-kb`. Start a new conversation and verify a private document
link from the current app.
[OpenAI marketplace commands](https://developers.openai.com/plugins/build/plugins).

## Claude

For a plugin installed through Claude web/desktop, use **Customize → Plugins**
to remove the old Spine installation and its old marketplace, then add
`https://github.com/spine-kb/plugins`, install Spine, and connect it through its
**Connectors** tab.

For a local Claude Code installation, replace the old catalog only if it is
listed by `claude plugin marketplace list`:

```sh
claude plugin marketplace remove spine-team-claude
claude plugin marketplace add spine-kb/plugins
claude plugin install spine-claude@spine-kb
```

Removing a Claude Code marketplace also uninstalls its plugins and removes saved
plugin data and settings. Review any data you need before removing it. Update
any project references to `spine-claude@spine-kb`, authenticate, and start a new
session.
[Claude Code migration commands](https://code.claude.com/docs/en/plugins/cli-reference).

## Antigravity and repository clones

For an existing clone, update its remote:

```sh
git remote set-url origin https://github.com/spine-kb/plugins.git
git pull --ff-only
agy plugin install ./plugins/spine-antigravity
```

Run the install command from the clone's root. New clones can follow the
[README](../README.md#antigravity-cli).

## New production connection

The production MCP endpoint is `https://app.spine-kb.com/mcp`. The former
`spine.pavorik.com` deployment and its connections are not preserved. Create or
update your client connection to the new endpoint and complete OAuth with your
current Spine account; installing the updated files does not authorize it. Copy
new document links from the app instead of rewriting an old host or path.

After reconnecting, check a known document in a new chat. Full installation,
OAuth, bootstrap delivery, and mobile behavior still need client-specific
verification against this production app; see [verification](verification.md).
