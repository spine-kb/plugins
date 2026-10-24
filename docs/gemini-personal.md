# Gemini: personal accounts on web and mobile

The target below is for the new app. The former deployment is gone; connect
after the new app is deployed and available. No new client authentication has
been verified.

Gemini web/mobile connects directly to remote MCP; the Antigravity GitHub plugin
does not install this connection or transfer its skill there.

The documented procedure is: Gemini web → Settings → Connected Apps → Custom
apps → Add a custom app → `https://app.spine-kb.com/mcp` → continue
authentication. With DCR support, client secrets do not need to be published
manually. Once connected, the custom app is available on web and mobile; an
explicit `@Spine` selects it for a request.
[Official instructions](https://support.google.com/gemini/answer/17209137?hl=en-yt).

As of 2026-10-22, Google lists these restrictions: a personal Google Account,
age 18+, location in the US, English, and Keep Activity enabled. Work/school
accounts are unsupported. Actual availability on team accounts, Spine
authentication, and carryover to mobile have not yet been verified. Google
currently specifies manual confirmation for write actions.

The server must provide clear instructions and tool descriptions, since delivery
of our CLI bootstrap skill to Gemini Apps has not been established. In a new
chat, test both a bare link and a link with `@Spine`: the selected tool, target
B from `/b/BASE/d/A/p/B`, the current guide, and interpretation of the document
together with the user's message. Test transfer of media from chat attachments
separately.
