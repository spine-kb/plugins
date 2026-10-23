# Spine team packages

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
