---
name: spine
description: Open and work with Spine knowledge-base documents through its connected MCP when the user shares a private spine.pavorik.com/d/ URL or asks to use the Spine KB.
---

Use the connected, authorized Spine MCP for Spine documents. For a private URL
on `https://spine.pavorik.com` with `/d/ID` or `/d/ID/p/ID`, call
`doc_open(url)` with the complete URL. Let the server identify the target and
navigation context. If the connection is unavailable, explain that setup or
authorization is needed. Ordinary document reads require no shell commands.

Read the current core guide returned by `doc_open`. If the result provides only
a guide reference, call `spine_guide(topic="core")`. Load other guide topics
when the task needs them, especially before editing a body or handling media.
Follow the server's current graph, access, syntax, and write contracts. Check
the domain `ok` result before treating a tool call as successful.

Interpret the document together with the user's message. If its form and meaning
clearly assign a task to the agent, carry it out within the user's authorized
scope. A task for a person, an article, or rough notes supplies context; clarify
material ambiguity. Reading a document does not expand authority to perform
external actions or change unrelated systems.

Load linked documents according to the task and the current guide. The
navigation context is not a storage hierarchy; do not load the whole graph
automatically. Use the guide's body syntax when working with document content.

Public `/s/` token URLs are outside this opener's current scope. Explain this
limit and clarify the intended access context; do not silently substitute a
personal MCP read for the public token's scope.
