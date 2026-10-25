# Connect Spine to ChatGPT

Connect your own Spine account to ChatGPT through a custom MCP plugin. The
production endpoint is `https://app.spine-kb.com/mcp`.

## Set up the connection

1. Sign in at [app.spine-kb.com](https://app.spine-kb.com) and confirm that you
   can access the base you want to use.
2. In ChatGPT web, open **Plugins → + → Add custom MCP server**.
3. Enter **Spine** as the name and `https://app.spine-kb.com/mcp` as the server
   URL. Select **OAuth** authentication and follow the setup prompts.
4. Create the plugin, install it from your personal plugins, and complete Spine
   sign-in and authorization when prompted.
5. Start a new chat, type `@`, select **Spine**, and ask it to read a private
   document link copied from the app.

This follows OpenAI's
[custom MCP connection instructions](https://developers.openai.com/api/docs/guides/custom-mcp-server).
Availability depends on your account and any workspace policies. If the custom
MCP option is unavailable, check the current client requirements.

## What this connection includes

The Git marketplace in this repository provides the `spine-openai` package for
local clients. Adding a custom MCP server in ChatGPT is a separate setup path;
it does not establish that the repository's bootstrap skill was installed. Web
archive import, independent-account installation, mobile availability, and
bootstrap delivery have not been verified for this release. See the
[verification record](verification.md).

Use an explicit Spine selection while checking the connection. Verify both a
bare document link and a link with a task in a new chat. Use a document you can
access; only request changes you intend to make. Package installation and OAuth
do not expand your Spine permissions.

After server tool metadata changes, refresh the plugin connection to obtain the
new tools and descriptions, then start a new chat. Current technical guides are
retrieved from Spine during use.
[Refresh and test a connection](https://developers.openai.com/plugins/deploy/connect-chatgpt).

## Moving from the former deployment

Old connections to `spine.pavorik.com` do not connect to the new production app.
Set up the new endpoint and authorize it with your current Spine account. See
[migration](migration.md) for the repository and marketplace changes.
