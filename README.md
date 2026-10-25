# Spine plugins

Connect your AI agent to [Spine](https://spine-kb.com) to read, write, and
navigate your knowledge bases. Share a document link, explore related documents,
or ask your agent to create and update content using your Spine account.

This public repository, [spine-kb/plugins](https://github.com/spine-kb/plugins),
provides separate importable marketplaces for OpenAI and Claude, plus an
Antigravity package. Each adapter connects to `https://app.spine-kb.com/mcp` and
includes the same short skill for working with Spine.

## Choose your agent

| Agent                        | Install from                                           | Package       |
| ---------------------------- | ------------------------------------------------------ | ------------- |
| Codex / OpenAI local desktop | OpenAI marketplace: `.agents/plugins/marketplace.json` | `spine`       |
| Claude and Claude Code       | Claude marketplace: `.claude-plugin/marketplace.json`  | `spine`       |
| Antigravity CLI              | Local plugin folder from this repository               | `spine`       |
| ChatGPT web                  | [Custom MCP connection](docs/chatgpt-personal.md)      | Account setup |
| Gemini web/mobile            | [Custom app connection](docs/gemini-personal.md)       | Account setup |

Both marketplaces use the ID `spine-kb`; each client reads its own catalog and
package format. The OpenAI marketplace appears as **SpineKb**. Antigravity
currently supports only its official named marketplace, so use the local-folder
installation below. ChatGPT web and Gemini use separate account connections.

The installation paths below follow the clients' documentation. End-to-end
installation and OAuth with the new production app have not yet been verified in
these clients. See [verification status](docs/verification.md).

## Before you connect

Sign in at [app.spine-kb.com](https://app.spine-kb.com) and make sure your
account can access the base you want to use. During setup, sign in to Spine and
complete OAuth for your own account. A plugin installation does not grant access
to someone else's bases or documents. Your agent works within the permissions
you authorize.

## Codex / OpenAI local desktop

Register the marketplace:

```sh
codex plugin marketplace add spine-kb/plugins
```

Open Plugins in the ChatGPT desktop app, select **SpineKb**, install **Spine**,
and complete authentication. Start a new conversation after installation.
[Official marketplace setup](https://developers.openai.com/plugins/build/plugins).

To refresh the registered source:

```sh
codex plugin marketplace upgrade spine-kb
```

Check the installed plugin in the desktop app after refreshing; a marketplace
refresh alone does not verify installation or authentication.

## Claude

In Claude web or desktop, open **Customize → Plugins → Add → Add marketplace**
and enter:

```text
https://github.com/spine-kb/plugins
```

Add **Spine**. Open the plugin's **Connectors** tab, add or connect Spine, and
complete OAuth. Account-installed plugins are documented to carry over to mobile
and Claude Code on the same account. Client and organization policies still
apply. [Claude installation and sync](https://claude.com/docs/plugins/overview).

For a local Claude Code installation, use:

```sh
claude plugin marketplace add spine-kb/plugins
claude plugin install spine@spine-kb
```

This CLI installation stays local; it does not install the plugin in your
claude.ai account.
[Claude Code commands](https://code.claude.com/docs/en/plugins/cli-reference).

## Antigravity CLI

Clone the repository and install its Antigravity adapter:

```sh
git clone https://github.com/spine-kb/plugins.git
cd plugins
agy plugin install ./plugins/spine-antigravity
```

Complete Spine authentication when prompted. The clone-and-folder route selects
the correct adapter from this repository's multiple packages.
[Antigravity installation](https://antigravity.google/docs/marketplace?tab=cli).

## Try Spine

Start a new conversation and ask your agent:

- “Use Spine to summarize this document: …” followed by its private link.
- “Use Spine to explain the context linked from this document: …”
- “Use Spine to update this document with the following changes: …”

Select the installed Spine plugin explicitly if your client does not activate it
automatically. Copy a private document link from the app; these links use
`https://app.spine-kb.com/b/BASE/d/ID` and may include navigation context.
Public `/s/` share links are not supported by the current plugin opener.

One connection can work with several bases. A document link identifies its base;
for a request without a link, name the base if you have several. The agent reads
that base's personal instructions and the current Spine guide before continuing.
When the task creates or changes documents, the result should include clickable
links to them.

## Updates and migration

Refresh the marketplace and update the installed package using your client's
plugin controls. For Claude account installs, use **Check for updates** in the
marketplace controls. Reconnect Spine if the client requests authorization.

All three adapters now use the plugin name `spine`. If you installed a package
with a provider suffix, used the earlier team catalogs, or connected to the
former production host, follow the [migration guide](docs/migration.md). The
catalogs still use `spine-kb`; provider suffixes remain only in this
repository's adapter directory names.

## Maintaining the packages

See [maintainer instructions](docs/maintaining.md) for the canonical skill,
adapter formats, branding, and validation commands, and
[verification](docs/verification.md) for evidence and remaining client checks.
