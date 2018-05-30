# Установка на локальную машину.
Данный проект будет использовать для защиты окончания курса python c нуля.
Я выбрал DJANGO,так как, Django - The web framework for perfectionists with  DEADLINE, я начал писать за неделю до сдачи :)

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
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
(env) $ python manage.py createsuperuser
(env) $ python manage.py runserver
```

Для выхода из локального окружения введите `exit`

#Основная идея:

После выполения builds(сборки приложения) или deploy(выкатки кода на stage or prod)  с помощью curl, POST-ом \
отправлять данные на приложения.

#Пример:

```
without token
curl -X POST http://localhost:8000/api/v1/ -d "author=1&project=build2&comment=fix link"

get token key

curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d 'username=admin&password=12qwaszx' 'http://localhost:8000/api/v1/rest-auth/login/' --insecure
{"key":"56cafc5028f96eee4c1c6a8f0bbdbf10960ce387"}

with
curl -X GET http://localhost:8000/api/v1/ -H  'Authorization: Token $token'
curl -X POST http://localhost:8000/api/v1/ -d "author=1&name=Dev1&project=build2&version=0.1&comment=fix link" -H 'Authorization: Token $token'
```

To be continues docker start

```
- docker-compose build
- docker-compose up -d
- docker-compose run web python manage.py makemigrations
- docker-compose run web python manage.py migrate
- docker-compose run web python manage.py createsuperuser
```
