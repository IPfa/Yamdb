# yamdb_final
yamdb_final

![yamdb_final workflow](https://github.com/IPfa/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# Описание

API для системы хранения отзывов
к произведениям культуры
Проект раворачивается через Docker. Смотри инструкции по установке.

# Шаблон наполнения env-файла

Для корректного старта контейнеров Docker необходимые следующие данные:

1. DB_ENGINE - в данном случае используется postgresql
2. DB_NAME=postgres - имя базы данных
3. POSTGRES_USEК - логин для подключения к базе данных
4. POSTGRES_PASSWORD - пароль для подключения к БД
5. DB_HOST=db - название сервиса контейнера в Docker
5. DB_PORT=5432 - порт для подключения к БД

# Установка

Клонировать репозиторий и перейти в него в командной строке.

Наполнить env-файл.

Запустите docker-compose:

```
docker-compose up
```

В новом окне терминала выполнить миграции:

```
docker-compose exec web python manage.py migrate --noinput
```

Импортировать базу данных из файла fixtures.json:

```
docker-compose exec web python manage.py loaddata fixtures.json
```

Собрать статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Открыть проект в браузере по адресу http://127.0.0.1/


# Авторы
[thelie](https://github.com/thelie) - управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail, поля.

[IPfa](https://github.com/IPfa) - категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты для них.

[firepanda70](https://github.com/firepanda70) - отзывы (Review) и комментарии (Comments): модели и view, эндпойнты, права доступа для запросов. Рейтинги произведений.

# Лицензия
MIT License