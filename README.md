1. docker-compose run  web django-admin.py startproject myweb2703 .
2. docker-compose run  web python manage.py migrate
3. docker-compose exec web python manage.py startapp firstapp 
4. docker-compose run  web python manage.py createsuperuser
5. docker-compose run  web python manage.py makemigrations
6. docker-compose run  web python manage.py migrate