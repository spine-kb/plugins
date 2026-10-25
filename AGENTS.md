# Spine plugins

This standalone repository is `https://github.com/spine-kb/plugins`. It
distributes client-specific packages for Spine users through separate OpenAI and
Claude marketplaces; both use the identifier `spine-kb`. OpenAI's marketplace
display name is `SpineKb`. Claude has no separate marketplace display-name
field; use `SpineKb` in its description. Package identities remain
`spine-openai`, `spine-claude`, and `spine-antigravity`.

Write user-facing documentation in English for people connecting their own Spine
accounts. Keep installation instructions in README and client guides; maintainer
details and historical evidence belong in `docs/maintaining.md` and
`docs/verification.md`. Do not describe documented client support as tested
installation or OAuth. The production MCP endpoint is
`https://app.spine-kb.com/mcp`.

`bootstrap/spine/SKILL.md` is the canonical skill. Keep all three adapter copies
byte-identical. Run the existing validator and formatting checks after package
changes; see `docs/maintaining.md`.

The approved Spine icon is packaged at `plugins/spine-openai/assets/spine.png`
and `plugins/spine-claude/assets/spine.png`. Keep these PNGs byte-identical;
OpenAI uses its copy for both `composerIcon` and `logo`, and Claude uses its
copy for the directory listing icon.

In the Hatch workstation, the canonical ready-to-use PNG is
`projects/spine/state/branding/spine-icon.png`; source provenance and all usage
paths are in `projects/spine/state/branding/README.md`. Copy that canonical file
unchanged when updating the packaged icons. Do not pick an alternative from
`misc`, historical OAuth drafts, or an image search, and do not redraw the logo.
A standalone clone already contains the approved packaged copies; the Hatch
branding directory is not a runtime or installation dependency.
