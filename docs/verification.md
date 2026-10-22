# Проверка локальных пакетов

Состояние на 2026-10-22: файлы подготовлены для отдельного репозитория
`spine-kb/team-plugins`. Пакеты не установлены; их выполнение на аккаунтах не
проверялось. В доступном авторизованном ChatGPT UI read-only просмотрены Add
menu и custom MCP form без создания подключения или загрузки архива. Запросы к
endpoint Spine не выполнялись; его доступность и OAuth остаются частью
клиентского прогона.

GitHub target `git@github.com:spine-kb/team-plugins.git` доступен с этой машины
по SSH и на момент подготовки не содержит refs. Неавторизованный GitHub API
вернул 404; публичность репозитория не подтверждена. Его доступность каждому
аккаунту и облачному клиенту проверяется отдельно. Настройки репозитория не
менялись.

## Статическая приёмка

`scripts/validate.py` проверяет JSON, две фактически загруженные официальные
схемы Agent Plugins, структуру тонких адаптеров, MCP URL, существование и
изоляцию относительных путей каталогов, отсутствие дополнительных
credential-bearing MCP полей, четыре одинаковых экземпляра bootstrap skill. Он
не подменяет нативную или поведенческую проверку клиента.

Схемы:

- <https://agent-plugins.org/schemas/1.0.0/plugin.schema.json>
- <https://agent-plugins.org/schemas/1.0.0/mcp.schema.json>

Antigravity schema URL из официальных docs
`https://antigravity.google/schemas/v1/plugin.json` вернул HTTP 404 при
проверке. Его manifest поэтому содержит только документированные `name` и
`description`; эти поля и конфигурация с `serverUrl` проверены по структуре
официальных примеров. Это **не** проверка загруженной Antigravity JSON Schema.
[Manifest](https://antigravity.google/docs/plugins/),
[MCP configuration](https://antigravity.google/docs/mcp/).

В полученной portable MCP schema `streamableHttpServer` запрещает дополнительные
поля, включая `extensions`, хотя OpenAI docs показывают OAuth настройки в
`extensions.com.openai.auth`. Local пакет сохраняет schema-valid минимум
`type` + `url`; OAuth discovery/DCR нужно подтвердить клиентом. Статические
credentials в пакет не добавляются.
[OpenAI authentication examples](https://developers.openai.com/plugins/build/plugins).

Claude manifest и `.mcp.json` сверены с
[официальным cross-surface примером](https://claude.com/docs/plugins/build).
Claude Code в этой среде отсутствует, поэтому `claude plugin validate` не
выполнялся и ради проверки не устанавливался. Каталоги OpenAI и Claude проверены
по их документированным полям и путям; для них не заявляется проверка через
недоступную официальную JSON Schema.

Skill дополнительно проходит `skill-creator/scripts/quick_validate.py` через
изолированный `uv run --no-project --with pyyaml`. Это проверяет frontmatter и
структуру, но не доказывает выбор нужного MCP моделью.

Фактический результат локальной приёмки:

- `uv run --no-project --with jsonschema scripts/validate.py` — успешно: 8
  JSON-файлов, обе загруженные схемы, 3 MCP-конфигурации, 2 каталога, 4
  одинаковых skill-файла.
- `quick_validate.py` — `Skill is valid!` для исходника и всех трёх копий.
- `DENO_NO_PACKAGE_JSON=1 deno fmt --check .` — успешно, 16 Markdown/JSON
  файлов. Два предупреждения workspace о недостающем `exports` в существующих
  backend manifests не относятся к пакетам.
- Просмотр состава пакетов — без секретов, статических bearer credentials,
  `.app.json` или placeholder app IDs. В manifests используются относительные
  источники; они существуют.

## Поведенческий прогон после установки

Записать версию клиента, способ установки, поверхность и фактические tool calls.
Проверить новый чат, OAuth и возобновление авторизации, голую ссылку, ссылку с
задачей и явное обращение к Spine, `/d/A/p/B`, отказ в доступе, задачу
агенту/человеку/статью/черновик, обновление metadata и guide. Публичный `/s/`
token не должен неявно заменяться личным чтением. Передача вложения и загрузка
большого файла — отдельные media-сценарии.
