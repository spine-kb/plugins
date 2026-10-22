# Spine: team packages

Packages for employees' separate personal accounts. The source is
[spine-kb/team-plugins](https://github.com/spine-kb/team-plugins), an
independent Git repository. The packages are not installed; their behavior on
accounts has not yet been verified.

To install a package, the repository must be accessible to the specific account
and client. Its public visibility has not been confirmed. SSH access from the
developer's machine does not confirm access from a cloud interface. The HTTPS
commands below assume the repository is accessible; a private repository
requires authentication supported by the client.

The configured endpoint is `https://spine.pavorik.com/mcp`. A direct read
through the existing connected Spine MCP succeeded in this Codex session; this
did not install or test these adapters. New OAuth flows, package installation,
bootstrap delivery, and behavior across client surfaces remain **unverified**.
The package files do not include server configuration or deployment. See
[verification details](docs/verification.md).

## What gets installed

The package combines a remote MCP declaration with a short English skill. The
skill activates for a private `spine.pavorik.com/d/...` link or a request to
work with the Spine KB, calls `doc_open`, retrieves the current server guide,
and reads related documents as needed for the task. The server supplies the
architecture, graph permissions, and body syntax. Users complete OAuth with
their own Spine accounts; installing a package grants no additional permissions.

The canonical text is [bootstrap/spine/SKILL.md](bootstrap/spine/SKILL.md). The
three adapters contain exact copies. After changing the source, update all three
copies and run the checks below. The packages do not use shell hooks, local MCP
processes, static tokens, or OpenAI app IDs.

| Client                                      | Package and catalog                                        | Installation                                                                                            |
| ------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Codex CLI / local desktop                   | `plugins/spine-openai`, `.agents/plugins/marketplace.json` | Add a Git/local marketplace, install the package, authenticate                                          |
| Claude personal web/desktop/mobile and Code | `plugins/spine-claude`, `.claude-plugin/marketplace.json`  | Add the marketplace through the web/desktop account, install the package, add and connect the connector |
| Antigravity CLI                             | `plugins/spine-antigravity`                                | Install the local folder after cloning, authenticate                                                    |
| ChatGPT personal web/mobile                 | [Separate account setup](docs/chatgpt-personal.md)         | A universal cloud package has not yet been built; cross-account installation needs verification         |
| Gemini personal web/mobile                  | [Direct URL connection](docs/gemini-personal.md)           | Each user adds a custom app in web and authenticates                                                    |

## Developer and icons

The developer name is **SpineDev**; the product name remains **Spine**. The
OpenAI adapter declares the supplied Spine logo as its interface logo and
composer icon. The Claude adapter declares the same logo for its directory
listing; Claude Code ignores this field at runtime, and versions earlier than
2.1.281 may warn about an unknown `icon` field. The minimal documented
Antigravity manifest has only `name` and `description`, so it declares neither
developer attribution nor an icon.
[OpenAI icons](https://developers.openai.com/plugins/deploy/submission#icons-and-screenshots),
[Claude directory listing fields](https://code.claude.com/docs/en/plugins/manifest-reference#directory-listing-fields),
[Antigravity manifest](https://www.antigravity.google/docs/plugins?tab=cli).

Actual icon rendering in clients has not been verified. Icon delivery for a
cloud custom MCP connection is independent of the packaged icons.

## Local installation for verification

The commands below are instructions for a future, separately agreed test run.
They were not executed while preparing the packages. From `team-plugins`:

```sh
codex plugin marketplace add .
codex
# In Codex, open /plugins, select Spine team · Codex, and install Spine.
```

Add the GitHub source with `codex plugin marketplace add spine-kb/team-plugins`.
[Official format and CLI](https://developers.openai.com/plugins/build/plugins).

For all Claude surfaces, start in web/desktop: Customize → Plugins → Add → Add
marketplace → `https://github.com/spine-kb/team-plugins` → add Spine. In the
package's Connectors tab, add/connect Spine and complete OAuth. Installation
from the account UI carries over to mobile and Claude Code on the same account;
installation only through the Code CLI does not carry back to claude.ai. The
local folder can be checked separately with
`claude plugin validate ./plugins/spine-claude`, if Claude Code is installed.
[Installation and sync](https://claude.com/docs/plugins/overview),
[remote connector format](https://claude.com/docs/plugins/build).

For Antigravity, clone the repository and install the adapter from its folder:

```sh
git clone https://github.com/spine-kb/team-plugins.git
cd team-plugins
agy plugin install ./plugins/spine-antigravity
```

For a CLI with SSH access configured, use:
`git clone git@github.com:spine-kb/team-plugins.git`.

Antigravity documents GitHub and local installation. For this repository with
multiple adapters, use a clone and local folder: installing a GitHub
subdirectory separately has not been confirmed. Arbitrary named marketplaces are
currently unsupported.
[Documentation](https://antigravity.google/docs/marketplace?tab=cli).

## Checks before installation

From `team-plugins`:

```sh
uv run --no-project --with jsonschema scripts/validate.py
DENO_NO_PACKAGE_JSON=1 deno fmt --check .
```

The first command fetches only two public Agent Plugins schemas; it does not
call the Spine endpoint. It checks JSON, MCP configurations, relative catalog
paths, and matching skills. Results and limitations are in
[docs/verification.md](docs/verification.md). After installation, a separate
client test run should check OAuth, a bare link, a link with a task, an explicit
request to Spine, and tool updates.

## Remaining work before distribution

Publish the current local changes when requested, install the packages, and run
the client tests. All catalog sources are relative; the manifests do not use app
IDs. No license has been chosen or added to the packages. For ChatGPT personal,
separately establish the supported cloud connection path and test an independent
account. Access to the GitHub package and access to the KB are controlled
independently.
