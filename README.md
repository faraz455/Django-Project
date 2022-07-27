# Django-Project
Markup :This is basic ___Django project___ which performs all the django functionalities to understand from Basic Django Rest Framework to Advance level. It contains ___Model View Templete___ architecture and ___Django Rest Framework___ as well

## Project Description

 Markup : - [x] Models
          - [x] Serializers
          - [x] Views
          - [x] Postgres DB
          - [x] Authentications
          - [x] Tokens (JWT)
          - [x] Exception Handling
          - [x] Cloudinary Storage
          - [x] Complex Queries
          - [x] Aysnc Operations


## To run code (Server)
Command: python3 manage.py runserver

## To create Super User
commanad: python3 manage.py createsuperuser

## To create App
command: python3 manage.py startapp <app Name>

## Make change in Model DB
command: python3 manage.py makemigrations
command: python3 manage.py migrate

## To run Celery 
command: celery -A mysite beat -l info 

## For Rabbitmq
command: sudo docker-compose up

## To free Port
command sudo kill -9 `sudo lsof -t -i:<port no>`