# Django-Project
This is basic ___Django project___ which performs all the django functionalities to understand from Basic Django Rest Framework to Advance level. It contains ___Model View Templete___ architecture and ___Django Rest Framework___ as well

## Project Descript
    - Models
    - Serializers
    - Views
    - Postgres DB
    - Authentications
    - Tokens (JWT)
    - Exception Handling
    - Cloudinary Storage
    - Complex Queries
    - Aysnc Operations

## To run code (Server)
``` ___Command:___ python3 manage.py runserver ```
## To create Super User
```___Command:___ python3 manage.py createsuperuser ```

## To create App
```___Command:___ python3 manage.py startapp <app Name> ```

## Make change in Model DB
```___Command:___ python3 manage.py makemigrations ```
```___Command:___ python3 manage.py migrate ```

## To run Celery 
```___Command:___ celery -A mysite beat -l info ``` 

## For Rabbitmq
```___Command:___ sudo docker-compose up ```

## To free Port
```___Command:___ sudo kill -9 `sudo lsof -t -i:<port no> ```
