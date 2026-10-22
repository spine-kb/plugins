# Spine: пакеты для команды

Пакеты для отдельных личных аккаунтов сотрудников. Источник —
[spine-kb/team-plugins](https://github.com/spine-kb/team-plugins), отдельный
Git-репозиторий. Пакеты не установлены; их работа на аккаунтах ещё не проверена.

Для установки репозиторий должен быть доступен конкретному аккаунту и клиенту.
Его публичность не подтверждена. Доступ по SSH с машины разработчика не
подтверждает доступ облачного интерфейса. HTTPS-команды ниже предполагают
доступность репозитория; для частного репозитория нужна поддерживаемая клиентом
авторизация.

Настроенный будущий endpoint — `https://spine.pavorik.com/mcp`. Его публичная
доступность, маршрутизация и OAuth из этих клиентов **не проверены**. Файлы
пакета не включают настройку или выкладку сервера.

## Что устанавливается

Пакет соединяет объявление remote MCP с коротким English skill. Skill
активируется по приватной ссылке `spine.pavorik.com/d/...` или запросу работы со
Spine KB, вызывает `doc_open`, получает актуальное руководство сервера и читает
связанные документы по смыслу задачи. Архитектура, права графа и body-синтаксис
поставляются сервером. Пользователь проходит OAuth под своим аккаунтом Spine;
установка пакета не предоставляет дополнительных прав.

Канонический текст — [bootstrap/spine/SKILL.md](bootstrap/spine/SKILL.md). Три
адаптера содержат его точные копии. После изменения исходника обновить все три
копии и выполнить проверку ниже. Пакеты не используют shell hooks, локальные
MCP-процессы, статические токены или OpenAI app IDs.

| Клиент                                    | Пакет и каталог                                            | Установка                                                                                         |
| ----------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Codex CLI / локальный desktop             | `plugins/spine-openai`, `.agents/plugins/marketplace.json` | Добавить Git/local marketplace, установить пакет, авторизоваться                                  |
| Claude personal web/desktop/mobile и Code | `plugins/spine-claude`, `.claude-plugin/marketplace.json`  | Добавить marketplace через web/desktop аккаунт, установить пакет, добавить и подключить connector |
| Antigravity CLI                           | `plugins/spine-antigravity`                                | Установить локальную папку после clone, авторизоваться                                            |
| ChatGPT personal web/mobile               | [Отдельный аккаунтный сценарий](docs/chatgpt-personal.md)  | Универсальный cloud-пакет пока не собран; способ cross-account установки требует проверки         |
| Gemini personal web/mobile                | [Прямое подключение URL](docs/gemini-personal.md)          | Каждый пользователь добавляет custom app в web и проходит авторизацию                             |

## Локальная установка для проверки

Команды ниже — инструкция для будущего согласованного прогона. В рамках
подготовки пакетов они не выполнялись. Из каталога `team-plugins`:

```sh
codex plugin marketplace add .
codex
# В Codex открыть /plugins, выбрать Spine team · Codex и установить Spine.
```

GitHub-источник добавляется командой
`codex plugin marketplace add spine-kb/team-plugins`.
[Официальный формат и CLI](https://developers.openai.com/plugins/build/plugins).

Для всех поверхностей Claude начать с web/desktop: Customize → Plugins → Add →
Add marketplace → `https://github.com/spine-kb/team-plugins` → добавить Spine. В
Connectors tab пакета добавить/подключить Spine и пройти OAuth. Установка из
аккаунтного UI переносится в mobile и Claude Code с тем же аккаунтом; установка
только через Code CLI обратно в claude.ai не переносится. Локальную папку можно
отдельно проверить командой `claude plugin validate ./plugins/spine-claude`,
если Claude Code установлен.
[Установка и синхронизация](https://claude.com/docs/plugins/overview),
[формат remote connector](https://claude.com/docs/plugins/build).

Для Antigravity клонировать репозиторий и установить адаптер из его папки:

```sh
git clone https://github.com/spine-kb/team-plugins.git
cd team-plugins
agy plugin install ./plugins/spine-antigravity
```

Для CLI с настроенным доступом по SSH команда клонирования:
`git clone git@github.com:spine-kb/team-plugins.git`.

Antigravity документирует GitHub и local install. Для текущего каталога с
несколькими адаптерами используется clone + локальная папка: установка GitHub
subdirectory отдельно не подтверждена. Произвольные именованные marketplaces
сейчас не поддержаны.
[Документация](https://antigravity.google/docs/marketplace?tab=cli).

## Проверки перед установкой

Из `team-plugins`:

```sh
uv run --no-project --with jsonschema scripts/validate.py
DENO_NO_PACKAGE_JSON=1 deno fmt --check .
```

Первый запуск получает только две публичные схемы Agent Plugins; endpoint Spine
он не вызывает. Проверяются JSON, конфигурации MCP, относительные пути каталогов
и совпадение skills. Результаты и ограничения — в
[docs/verification.md](docs/verification.md). После установки отдельный
клиентский прогон должен проверить OAuth, голую ссылку, ссылку с задачей, явное
обращение к Spine и обновление инструментов.

## Что остаётся для распространения

Установить пакеты и выполнить клиентский прогон. Все catalog sources
относительные; app IDs в manifests не используются. Лицензия не выбрана и в
пакеты не добавлена. Для ChatGPT personal отдельно установить поддерживаемый
путь облачного подключения и проверить независимый аккаунт. Доступ к
GitHub-пакету и доступ к KB регулируются независимо.
