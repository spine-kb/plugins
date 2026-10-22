# ChatGPT: personal accounts

Employees have separate personal accounts. A shared workspace here would mean a
ChatGPT organization with an administrator and a managed catalog; the selected
setup does not assume one.

## Direct MCP connection

The current official developer flow describes creating a connection in ChatGPT
web: Plugins → Add custom MCP server → name Spine → URL
`https://spine.pavorik.com/mcp` → OAuth → Create as a plugin → Install. Then
open a new chat and select `@Spine`. This is the documented procedure.
[Add custom MCP server](https://developers.openai.com/api/docs/guides/custom-mcp-server).

A read-only inspection of the available account's authenticated UI on 2026-10-22
confirmed Plugins → Add → Create plugin, Upload plugin archive, and Add custom
MCP server. The custom MCP form shows Server URL/Tunnel, OAuth, and additional
OAuth settings. During that initial inspection, no connection was created, ZIP
accepted, OAuth completed, or Spine calls made. These controls do not require a
shared workspace or team administrator for this scenario.

A later attempt to open the ChatGPT Plugins page failed with "ChatGPT hit a
snag". The web archive installation route remains untested. Separately, a direct
`mcp__codex_apps__spine_doc_open` call through the existing connected MCP
succeeded in this Codex session with `structuredContent.ok=true`. No new OAuth
flow, write, or client package installation was performed. This read does not
verify ChatGPT web archive installation, independent personal accounts, mobile,
or bootstrap skill delivery and bare-link tool selection.

The official pages do not provide a consistent matrix of personal plans and
surfaces. Help describes custom MCP for Business/Enterprise/Edu and web only,
but the same page's FAQ allows Pro read/fetch. The developer flow mentions
personal plugins and read/write tools subject to account policies. Full write
support and mobile support for personal custom MCP therefore remain unverified
capabilities.
[Help: connecting custom MCP](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt).

## Role of the GitHub package

The Git marketplace in this repository is intended for local Codex/desktop
clients. It is not a proven way to install a cloud integration in personal
web/mobile. Direct GitHub import was not observed in the inspected Add menu;
this does not prove it is absent from every UI. The documented workspace import
is a separate method. Personal Upload plugin archive is visible, but the
accepted archive format and the capabilities of a package installed through it
have not yet been verified.
[GitHub import](https://learn.chatgpt.com/docs/enterprise/plugin-management),
[upload and surface limitations](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt).

No documented solution has been established for personal cross-account remote
sharing and reuse of a single app ID. This repository therefore has no
`.app.json`, invented shared registration, or cloud manifest with a placeholder.
Public directory submission after review is a separate documented distribution
method; it has not been selected or performed.
[Publication](https://developers.openai.com/plugins/deploy/submission).

## What to verify on an available account

After separately agreeing to create a connection, complete OAuth, check reading
and writing a test document in web, then test the same account in desktop/mobile
and an independent personal account. Separately check installation of the
bootstrap skill and selection of `doc_open` from a bare link. The presence of
MCP alone does not prove skill delivery or transfer of chat attachments.

After tool metadata changes, the official custom connection flow requires
refreshing the connection and starting a new chat. The guide text is retrieved
from the server during use, so updating the guide does not require a copy in the
skill.
[Testing and refreshing metadata](https://developers.openai.com/plugins/deploy/connect-chatgpt).
