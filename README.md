# Yamdb
REST API web application Yamdb developed on Python. Yamdb is a system to collect the reviews to various works of art, such as films, books, music albums and so on. Application has following functionality: creating and editing users, works of art, categories, comments, reviews and genres. Users could also be separated in different groups depending of what rights they should have.  This learning project was written in team of 3 developers and it is a reference to famous IMDm.com.

# Technology Stack
Python, Django, Django REST, SQLite, PostgreSQL, Docker, NGNIX.

# Launching
For launch Docker application is needed.
Create env-file. Please see env-file template.
Start docker-compose:
```
docker-compose up -d --build
```
Perform migrations:
```
docker-compose exec web python manage.py migrate
```
Collect static files:
```
docker-compose exec web python manage.py collectstatic --no-input
```
Create Superuser:
```
docker-compose exec web python manage.py createsuperuser
```
**You can log in there:**
http://localhost/admin/

# Tamplate for env-файла
For correct functionality of Docker following data is needed:

1. DB_ENGINE - in our case this is postgresql (default: django.db.backends.postgresql)
2. DB_NAME - database name (default: postgres)
3. POSTGRES_USER - login for database connection (default: postgres)
4. POSTGRES_PASSWORD - password for database connection (default: Password1)
5. DB_HOST - name of service container in Docker (default: db)
5. DB_PORT - port for the database connection (default: 5432)

# Authors
[thelie](https://github.com/thiele) - user managment (Auth и Users): registration and authentication system, access rights, token handling, e-mail confirmation system.
[IPfa](https://github.com/IPfa) - Categories, Genres and Titles: models, views and endpoints for them.
[firepanda70](https://github.com/firepanda70) - Reviews and Comments: models and views, endpoints, access rights for queries. Ratings of Titles.