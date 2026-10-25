# Connect Spine to Gemini

Gemini web/mobile connects directly to Spine's remote MCP endpoint. Installing
the Antigravity plugin does not install this account connection or deliver its
skill to Gemini Apps.

## Availability

Google's documentation checked on 2026-10-25 requires a personal Google Account,
age 18 or over, a location in the US, English, and **Keep Activity** enabled.
Work and school accounts are currently unsupported. Check the
[current requirements](https://support.google.com/gemini/answer/17209137?hl=en-yt)
before starting.

## Set up the connection

1. Sign in at [app.spine-kb.com](https://app.spine-kb.com) and confirm access to
   the base you want to use.
2. In Gemini web, open **Settings → Connected Apps**. Some accounts show this
   under **Personal Intelligence → Connected Apps**.
3. Under **Custom apps**, add `https://app.spine-kb.com/mcp`.
4. Continue through the prompts and complete Spine sign-in and authorization.
5. In a new chat, type `@`, select Spine, and ask it to read a private document
   link from your base.

Google documents that a custom app connected in web is also available in the
mobile app, and that write actions require manual confirmation.
[Official setup](https://support.google.com/gemini/answer/17209137?hl=en-yt).

## Verification status

Spine OAuth, mobile carryover, bootstrap delivery, and attachment transfer have
not been verified in Gemini against the new production app. A connection alone
does not prove those behaviors. See [verification](verification.md) for the
client checks still needed.

If you connected the former `spine.pavorik.com` deployment, set up the new
endpoint and authorize it with your current account. See
[migration](migration.md).
