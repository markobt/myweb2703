# Установка на локальную машину. Данный проект будет использовать для защиты окончания курса python c нуля.
# Я выбрал DJANGO,так как, DjangoThe web framework for perfectionists with  DEADLINE, я начал писать за неделю до сдачи :)

Перед установкой, Вам нужно скачать репозиторий.

```
$ git clone git@github.com:markobt/myweb2703.git
```

Потом перейти  `cd myweb2703` в текущую директорию и запустить локальное окружения `pipenv shell` далее установить пакеты `pipenv install`.
Накатить миграции `python manage.py migrate`, далее создать супер юзера `python manage.py createsuperuser` и запустить сервер `python manage.py runserver`.

```
$ cd myweb2703
$ pipenv shell
(env) $ pipenv install
(env) $ python manage.py migrate
(env) $ python manage.py createsuperuser
(env) $ python manage.py runserver
```

Для выхода из локального окружения введите `exit`


To be continues docker start

```
- docker-compose build
- docker-compose up -d
- docker-compose run  web django-admin.py startproject myweb2703 .
- docker-compose run  web python manage.py migrate
- docker-compose exec web python manage.py startapp todos
- docker-compose run  web python manage.py createsuperuser
- docker-compose run  web python manage.py makemigrations
- docker-compose run  web python manage.py migrate
- docker-compose exec web python manage.py startapp api
```