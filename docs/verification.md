# Local package verification

Status as of 2026-10-22: the adapters and documentation are in English, with
SpineDev attribution in supported metadata and the original Spine PNG packaged
for OpenAI and Claude. The packages have not been installed or behaviorally
verified on client accounts. The current translation and branding changes remain
local and have not been pushed.

During initial preparation, a read-only inspection of the available
authenticated ChatGPT UI covered the Add menu and custom MCP form without
creating a connection or uploading an archive. No requests were made to the
Spine endpoint during that preparation. A later attempt to open the ChatGPT
Plugins page failed with "ChatGPT hit a snag"; web archive installation remains
untested.

The GitHub target `git@github.com:spine-kb/team-plugins.git` is accessible from
this machine over SSH. It had no refs during initial preparation; a later
`git ls-remote` check confirmed that `main` now exists. The initial
unauthenticated GitHub API request returned 404; public visibility remains
unconfirmed. Access for each account and cloud client is checked separately.
Repository settings were not changed.

## Direct connected MCP read

A direct `mcp__codex_apps__spine_doc_open` call through the existing connected
Spine MCP succeeded in this Codex session on a private document, returning
`structuredContent.ok=true`. No private document identifiers or content are
recorded here. No new OAuth flow, write, or client package installation
occurred.

This single read confirms access through that existing connection. It does not
verify installation of the team-plugins adapters, bootstrap delivery, selection
of `doc_open` from a bare link, web ZIP installation, independent personal
accounts, mobile behavior, or icon rendering. The bootstrap skill already
contains its domain trigger and was unchanged, but this session's skill catalog
did not expose it. The cause of that installation or delivery gap remains
unresolved.

## Static acceptance checks

`scripts/validate.py` checks JSON, two actually downloaded official Agent
Plugins schemas, the structure of the thin adapters, the MCP URL, the existence
and isolation of relative catalog and icon paths, SpineDev attribution in
supported metadata, the absence of additional credential-bearing MCP fields, and
four identical copies of the bootstrap skill. It does not replace native client
validation or behavioral testing.

Schemas:

- <https://agent-plugins.org/schemas/1.0.0/plugin.schema.json>
- <https://agent-plugins.org/schemas/1.0.0/mcp.schema.json>

The Antigravity schema URL from the official docs,
`https://antigravity.google/schemas/v1/plugin.json`, returned HTTP 404 when
checked. Its manifest therefore contains only the documented `name` and
`description`; these fields and the configuration with `serverUrl` were checked
against the structure of the official examples. This is **not** validation
against a downloaded Antigravity JSON Schema.
[Manifest](https://antigravity.google/docs/plugins/),
[MCP configuration](https://antigravity.google/docs/mcp/).

In the retrieved portable MCP schema, `streamableHttpServer` forbids additional
fields, including `extensions`, although OpenAI docs show OAuth settings in
`extensions.com.openai.auth`. The local package keeps the schema-valid minimum
of `type` + `url`; OAuth discovery/DCR needs client verification. Static
credentials are not added to the package.
[OpenAI authentication examples](https://developers.openai.com/plugins/build/plugins).

The Claude manifest and `.mcp.json` were checked against the
[official cross-surface example](https://claude.com/docs/plugins/build). Claude
Code is absent from this environment, so `claude plugin validate` was not run,
and Claude Code was not installed for verification. The OpenAI and Claude
catalogs were checked against their documented fields and paths; no validation
against an unavailable official JSON Schema is claimed for them.

The skill also passes `skill-creator/scripts/quick_validate.py` through isolated
`uv run --no-project --with pyyaml`. This checks frontmatter and structure but
does not prove that the model selects the correct MCP.

Initial preparation acceptance results:

- `uv run --no-project --with jsonschema scripts/validate.py` — passed: 8 JSON
  files, both downloaded schemas, 3 MCP configurations, 2 catalogs, and 4
  identical skill files.
- `quick_validate.py` — `Skill is valid!` for the source and all three copies.
- `DENO_NO_PACKAGE_JSON=1 deno fmt --check .` — passed, 16 Markdown/JSON files.
  Two workspace warnings about missing `exports` in existing backend manifests
  are unrelated to the packages.
- Package contents reviewed: no secrets, static bearer credentials, `.app.json`,
  or placeholder app IDs. The manifests use relative sources, which exist.

## Current translation and branding checks

The completed local checks after the translation and branding changes passed:

- `uv run --no-project --with jsonschema scripts/validate.py`: 8 JSON files,
  both downloaded official schemas, 3 MCP adapters, 2 catalogs, and 4 identical
  skills. The updated checks cover SpineDev attribution and contained icon
  paths. This command contacted only schema endpoints, not clients or Spine.
- Both packaged PNGs were confirmed byte-identical to the supplied original.
- The repository Cyrillic scan found no matches.
- `DENO_NO_PACKAGE_JSON=1 deno fmt --check .`: 16 files passed. The same two
  existing backend workspace warnings about missing `exports` were unrelated to
  these packages.
- `git diff --check` passed.

The packaged OpenAI icons and Claude directory listing icon are configured;
actual rendering remains unverified. Claude Code ignores its directory listing
icon at runtime; older versions may warn about the field. Antigravity keeps its
minimal documented manifest. See the
[branding details](../README.md#developer-and-icons).

## Behavioral testing after installation

Record the client version, installation method, surface, and actual tool calls.
Test a new chat, OAuth and reauthorization, a bare link, a link with a task, an
explicit request to Spine, `/d/A/p/B`, access denial, tasks involving an agent,
human, article, or draft, and metadata and guide updates. A public `/s/` token
must not be silently replaced with personal reading access. Attachment transfer
and large file upload are separate media scenarios.
