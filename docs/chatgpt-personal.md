# ChatGPT: личные аккаунты

У сотрудников отдельные personal аккаунты. Общий workspace здесь означал бы
организацию ChatGPT с администратором и управляемым каталогом; для выбранной
схемы он не предполагается.

## Прямое подключение MCP

Текущий официальный developers flow описывает создание подключения через ChatGPT
web: Plugins → Add custom MCP server → имя Spine → URL
`https://spine.pavorik.com/mcp` → OAuth → Create as a plugin → Install. Затем
открыть новый чат и выбрать `@Spine`. Это документированный порядок.
[Add custom MCP server](https://developers.openai.com/api/docs/guides/custom-mcp-server).

В авторизованном UI доступного аккаунта 2026-10-22 read-only подтверждены
Plugins → Add → Create plugin, Upload plugin archive и Add custom MCP server.
Форма custom MCP показывает Server URL/Tunnel, OAuth и дополнительные OAuth
настройки. Создание подключения, принятие ZIP, OAuth и вызовы Spine не
выполнялись. Эти controls не требуют для этого сценария общего workspace или
администратора команды.

Официальные страницы не дают согласованной personal plan/surface matrix. Help
описывает custom MCP для Business/Enterprise/Edu и web-only, но FAQ той же
страницы допускает Pro read/fetch. Developers flow говорит о personal plugins и
read/write tools subject to account policies. Поэтому full write и mobile для
personal custom MCP пока остаются непроверенными возможностями.
[Help: подключение custom MCP](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt).

## Роль GitHub-пакета

Git marketplace из этого каталога предназначен для локальных Codex/desktop
клиентов. Он не является доказанной установкой cloud-интеграции в personal
web/mobile. Прямой GitHub import в просмотренном Add menu не наблюдался; это не
доказывает его отсутствие во всех UI. Документированный workspace import
является отдельным способом. Personal Upload plugin archive виден, но
принимаемый формат архива и возможности установленного через него пакета ещё не
проверены.
[GitHub import](https://learn.chatgpt.com/docs/enterprise/plugin-management),
[upload и ограничения поверхности](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt).

Для personal cross-account remote sharing и повторного использования одного app
ID документированное решение не установлено. Поэтому здесь нет `.app.json`,
выдуманной общей регистрации или cloud manifest с placeholder. Публичная
directory submission после review — отдельный документированный способ
распространения; он пока не выбран и не выполнялся.
[Публикация](https://developers.openai.com/plugins/deploy/submission).

## Что проверить на доступном аккаунте

После отдельного согласования создания подключения пройти OAuth, проверить
чтение и запись тестового документа в web, затем тот же аккаунт в desktop/mobile
и независимый personal аккаунт. Отдельно проверить установку bootstrap skill и
выбор `doc_open` по голой ссылке. Наличие MCP само по себе не доказывает
доставку skill или передачу чат-вложений.

После изменения tool metadata официальный custom-connection flow требует Refresh
подключения и нового чата. Текст guide извлекается с сервера при работе, поэтому
обновление guide не требует его копии в skill.
[Проверка и обновление metadata](https://developers.openai.com/plugins/deploy/connect-chatgpt).
