# Local package verification

## Current target (2026-10-24)

The former production deployment is gone. Packages target
`https://app.spine-kb.com/mcp` and private `/b/BASE/d/...` URLs. Earlier
connected reads below describe historical evidence, not a live current
connection. New OAuth, installation and runtime behavior must be checked after
deployment.

The canonical skill now uses `spine_bases` and `spine_bootstrap` for multiple
bases and base-local personal documents. Public `/s/` links remain a separate
scope. No client installations, real-account authentication or production calls
were performed for this change.

## Shared-app package checks (2026-10-24)

`uv run --no-project --with jsonschema scripts/validate.py` passed after the
endpoint/skill changes: 8 JSON files, both fetched official schemas, 3 MCP
adapters, 2 catalogs and 4 byte-identical skill copies. The expected endpoint is
now `https://app.spine-kb.com/mcp`. OpenAI and Claude package versions are
0.2.0; no unsupported version field was added to the minimal Antigravity
manifest. `DENO_NO_PACKAGE_JSON=1 deno fmt --check .` and `git diff --check`
passed. Only official schema endpoints were contacted by these package checks.

The canonical skill covers explicit and unambiguous base selection, one-base
auto-selection, refusal without fallback, base-switch bootstrap, full personal
body reading and revision-triggered rereading. It preserves current technical
guide loading, public-token separation, task authorization and final result-link
instructions. Earlier related uncommitted interaction/link guidance was retained
in the canonical source and all three adapters as part of the coherent wave.
Static checks prove packaging and equality, not actual model compliance.

The backend's synthetic SQL and real SDK/HTTP checks validate the server-side
multi-base/bootstrap contract separately; console browser checks validate its
base routes. No new package was installed in Codex, Claude or Gemini and no real
OAuth/client account was used. After deployment, verify installation, selected
base, initial context, changed revision, no fallback and mobile behaviour on
each supported client surface. Historical evidence below does not establish the
new endpoint's availability.

Status as of 2026-10-23: the adapters and documentation are in English, with
SpineDev attribution in supported metadata and the corrected, cropped Spine PNG
packaged for OpenAI and Claude. The packages have not been installed or
behaviorally verified on client accounts. The icon correction is published in
the repository; unrelated local bootstrap changes are excluded.

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

## Historical translation and branding checks (2026-10-22)

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

## Corrected icon checks (2026-10-23)

The previous packaged image was the wrong logo. Both packaged PNGs now exactly
copy the approved, centered 512×512 RGBA icon from the Hatch workstation path
`projects/spine/state/branding/spine-icon.png`. Its SHA-256 is
`8e27c0a1e58311c9837f4d3fb501351741f36aa243a938dbd3c43c9e93cb5c14`. The original
and usage paths are recorded in the adjacent Hatch branding README; they are not
an installation dependency of this standalone repository.

- Both package copies are byte-identical to the canonical icon. OpenAI's
  `composerIcon` and `logo` resolve to its one packaged copy; Claude's `icon`
  resolves to its matching copy. Manifest paths are unchanged.
- `uv run --no-project --with jsonschema scripts/validate.py` passed on the
  isolated publication tree: 8 JSON files, both downloaded schemas, 3 MCP
  adapters, 2 catalogs, and 4 identical skills. Only schema endpoints were
  contacted.
- `DENO_NO_PACKAGE_JSON=1 deno fmt --check .` and `git diff --check` passed.
- Client installation and actual icon rendering remain unverified.

## Behavioral testing after installation

Record the client version, installation method, surface, and actual tool calls.
Test a new chat, OAuth and reauthorization, a bare link, a link with a task, an
explicit request to Spine, `/d/A/p/B`, access denial, tasks involving an agent,
human, article, or draft, and metadata and guide updates. A public `/s/` token
must not be silently replaced with personal reading access. Attachment transfer
and large file upload are separate media scenarios.
