<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center"><code>❯ HEADLINE TEST </code></h1></p>
<p align="center">
	<em><code>❯ NEWS BOT</code></em>
</p>
<p align="center">
	<!-- local repository, no metadata badges. --></p>
<p align="center">Built with the tools and technologies:</p>
<p align="center">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=default&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/SQLAlchemy-D71F00.svg?style=default&logo=SQLAlchemy&logoColor=white" alt="SQLAlchemy">
	<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style=default&logo=Pytest&logoColor=white" alt="Pytest">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=default&logo=Docker&logoColor=white" alt="Docker">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style=default&logo=AIOHTTP&logoColor=white" alt="AIOHTTP">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=default&logo=Pydantic&logoColor=white" alt="Pydantic">
</p>
<br>

##  Оглавление

- [ Введение](#введение)
- [ Структура проекта](#структура-проекта)
- [ Начало работы](#начало-работы)
  - [ Зависимости](#необходимые-зависимости)
  - [ Установка](#установка)
  - [ Использование](#использование)
  - [ Тестирование](#тестирование)
- [ Мои оправдания](#мои-оправдания)


---

##  Введение

Этот проект - тестовое задание от компании HEADLINES.
С каких ресурсов собираются новости:
- NBC
- RIA
- LENTA

Изъянов много, но штука рабочая.

---


##  Структура проекта

```sh
└── /
    ├── Dockerfile
    ├── alembic.ini
    ├── app.py
    ├── docker-compose.yml
    ├── migrations
    │   ├── README
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    ├── requirements.txt
    ├── settings.py
    ├── src
    │   ├── bot.py
    │   ├── buttons.py
    │   ├── database.py
    │   ├── logger.py
    │   ├── models.py
    │   ├── repositories
    │   ├── routers
    │   ├── scheduler.py
    │   ├── sources
    │   ├── states.py
    │   └── templates.py
    └── tests
        ├── __init__.py
        ├── conftest.py
        └── services
```

---
##  Начало работы

###  Необходимые зависимости

Перед началом работы у Вас должны быть установлены:

- Docker


###  Установка

1. Клонируйте репозиторий:
```sh
❯ git clone ../
```

2. Перейдите в папку с проектом:
```sh
❯ cd 
```

3. Создайте файл `.env` в корневом каталоге

```
BOT_TOKEN="your_bot_token"
POSTGRES_USER=test_user
POSTGRES_PASSWORD=test_password
POSTGRES_DB=test_news_database
POSTGRES_PORT=5432
POSTGRES_HOST=database
```
4. Соберите проект через `docker-compose`
```sh
❯ docker compose build
```

5. Запустите миграции
```sh
❯ docker compose run --rm bot alembic upgrade head
```

6. Добавьте в базу данных следующие источники (`source` таблица):

| id | title |  url  |
|:---|:-----:|:-----:|
| 1  | LENTA | https://lenta.ru/ |
| 2  |  NBC  |https://www.nbcnews.com/ |
| 3  |  RIA  | https://ria.ru/ |

###  Использование
**Используя `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker compose up
```

###  Тестирование
На данный момент тесты не **работают**.
```sh
❯ docker compose run --rm bot pytest
```
---
## Мои оправдания

Что мне не нравится?
- Нужно в ручную заносить источники в БД. Я хотел это исправить, но я не успел.
- В целом структура проекта. Я бы над ней подумал еще.
- Интерфейс. Это понятно, ибо я делал на скорую руку.

Что можно сделать?
- Добавить возможность регулировать настройки выдаваемых новостей.
- Записывать действия пользователей в БД. Я подумал, что логи тоже не плохой вариант.
- Написать тесты
- Сделать все `repositories` репозиториями. Сейчас там только лишь `news.py` имеет нужную форму.
- Сделать более приемлемый внешний вид бота. Добавить Jinja, emoji и прочее.
- Добавить возможность фильтрации по темам новостей (business, sport etc.)
- Подключить pool прокси, грамотно обрабатывать ошибки.

В целом я не буду скрывать, я тут постарался показать как можно больше своих skills, но не смог. Поздно начал и хотел уложиться в дедлайн. + перфекционизм. 





