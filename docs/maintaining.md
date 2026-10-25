# Maintain Spine plugins

The public source is [spine-kb/plugins](https://github.com/spine-kb/plugins). In
Hatch it is an independent Git repository at `projects/spine/plugins/`. The
packages connect to `https://app.spine-kb.com/mcp`; backend code and
knowledge-base content live outside this repository.

## Package layout

- `.agents/plugins/marketplace.json`: OpenAI catalog, ID `spine-kb`, display
  name `SpineKb`, exposing `spine-openai`.
- `.claude-plugin/marketplace.json`: Claude catalog, ID `spine-kb`, exposing
  `spine-claude`. Claude does not define a separate marketplace display-name
  field; its description names `SpineKb`.
- `plugins/spine-antigravity/`: local-folder adapter for Antigravity.
- `bootstrap/spine/SKILL.md`: canonical English skill, copied byte-for-byte to
  `plugins/<package>/skills/spine/SKILL.md` in all three adapters.

Keep the two marketplaces separate and use each client's native package format.
The skill covers activation, base selection, base-local personal context, task
interpretation, and delivery of result links. Technical contracts for the graph,
permissions, document syntax, writes, and media come from the server guides. The
adapters contain no shell hooks, local MCP processes, static credentials, or
OpenAI app IDs. Installing a package grants no Spine permissions.

OpenAI and Claude package versions are `0.3.0`. Antigravity keeps its minimal
manifest with only `name` and `description`; do not add an unsupported version
field. Marketplace renaming requires the [migration steps](migration.md), even
when the package names stay unchanged.

No license has been selected or added to this repository.

## Attribution and icons

The developer name is **SpineDev**, and the product name is **Spine**. OpenAI
uses its packaged PNG for `composerIcon` and `logo`. Claude declares the same
PNG as its directory listing icon. Antigravity's minimal manifest declares no
icon or developer field. Client rendering has not been verified.

The approved PNG is packaged at `plugins/spine-openai/assets/spine.png` and
`plugins/spine-claude/assets/spine.png`. Keep these copies byte-identical. In
Hatch the canonical ready-to-use source is
`projects/spine/state/branding/spine-icon.png`; provenance and usage paths are
recorded in the adjacent branding README. Copy it unchanged. A standalone clone
already contains the approved copies and does not need the Hatch directory.

## Check a change

From this repository's root:

```sh
uv run --no-project --with jsonschema scripts/validate.py
DENO_NO_PACKAGE_JSON=1 deno fmt --check .
git diff --check
```

The validator checks the two downloaded Agent Plugins schemas, JSON, adapter and
catalog paths, marketplace identities, MCP endpoints, icon paths, publisher
metadata, and exact skill copies. It contacts only the schema endpoints. These
checks do not install plugins, authenticate accounts, or call Spine.

When Claude Code is available, native validation can additionally check the
catalog and package with `claude plugin validate .` and
`claude plugin validate ./plugins/spine-claude`. Native validation and actual
client behavior are separate from the static checks recorded in
[verification](verification.md).

## Client acceptance

Record client version, surface, install/update method, and actual tool calls.
Check OAuth, a new chat, a bare link, a link with a task, explicit Spine
selection, target B in `/b/BASE/d/A/p/B`, and denied access without base
fallback. Also check multi-base selection, personal bootstrap and revision
updates, and clickable links to saved results. Check mobile and media transfer
separately. Do not treat documented support or a historical connection as a
verified new installation. Current limitations and earlier evidence belong in
[verification](verification.md).
