# Yamdb

REST API веб приложения Yamdb написанный на Python. Yamdb - это системы хранения отзывов к произведениям культуры. Проект создавался командой из трех разработчиков.

# Стек Технологий
Python, Django, Django REST, SQLite, PostgreSQL, Docker, NGNIX.

# Запуск
Для запуска проекта необходим Docker.
Наполнить env-файл. Смотри шаблон ниже.
Запустить docker-compose:
```
docker-compose up -d
```
Выполнить миграции:
```
docker-compose exec web python manage.py migrate
```
Собрать статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
**Проект доступен по адресу:**
http://127.0.0.1/

# Шаблон наполнения env-файла
Для корректного старта контейнеров Docker необходимые следующие данные:

1. DB_ENGINE - в данном случае используется postgresql (default: django.db.backends.postgresql)
2. DB_NAME - имя базы данных (default: postgres)
3. POSTGRES_USER - логин для подключения к базе данных (default: postgres)
4. POSTGRES_PASSWORD - пароль для подключения к БД (default: Password1)
5. DB_HOST - название сервиса контейнера в Docker (default: db)
5. DB_PORT - порт для подключения к БД (default: 5432)

# Авторы
[thelie](https://github.com/thiele) - управление пользователями (Auth и Users): система регистрации и аутентификации, права доступа, работа с токеном, система подтверждения e-mail, поля.
[IPfa](https://github.com/IPfa) - категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты для них.
[firepanda70](https://github.com/firepanda70) - отзывы (Review) и комментарии (Comments): модели и view, эндпойнты, права доступа для запросов. Рейтинги произведений.