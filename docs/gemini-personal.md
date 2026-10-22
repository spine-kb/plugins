# Gemini: личные аккаунты в web и mobile

Gemini web/mobile подключается прямо к remote MCP; GitHub-плагин Antigravity не
устанавливает это подключение и не переносит туда свой skill.

Документированный порядок: Gemini web → Settings → Connected Apps → Custom apps
→ Add a custom app → `https://spine.pavorik.com/mcp` → дальнейшая авторизация.
При поддержке DCR не требуется вручную публиковать клиентские секреты. После
подключения custom app доступен в web и mobile; явное `@Spine` позволяет выбрать
его для запроса.
[Официальная инструкция](https://support.google.com/gemini/answer/17209137?hl=en-yt).

На 2026-10-22 Google указывает ограничения: personal Google Account, возраст
18+, нахождение в US, English и включённый Keep Activity. Work/school accounts
не поддержаны. Фактическая доступность в аккаунтах команды, авторизация Spine и
перенос в mobile ещё не проверены. Для write actions Google сейчас указывает
ручное подтверждение.

На сервере должны быть понятные instructions и tool descriptions, поскольку
доставка нашего CLI bootstrap skill в Gemini Apps не установлена. Проверить на
новом чате как голую ссылку, так и ссылку с `@Spine`: выбранный инструмент,
целевой B из `/d/A/p/B`, актуальный guide и интерпретацию документа вместе с
сообщением пользователя. Передачу медиа из чат-вложения проверять отдельно.
