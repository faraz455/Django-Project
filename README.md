# Django-Project
This is basic ___Django project___ which performs all the django functionalities to understand from Basic Django Rest Framework to Advance level. It contains ___Model View Templete___ architecture and ___Django Rest Framework___ as well

## Project Description
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

### To run code (Server)
``` python3 manage.py runserver ```
### To create Super User
```python3 manage.py createsuperuser ```

### To create App
```python3 manage.py startapp <app Name> ```

### Make change in Model DB
```python3 manage.py makemigrations ```
```python3 manage.py migrate ```

### To run Celery 
```celery -A mysite beat -l info ``` 

### For Rabbitmq
```sudo docker-compose up ```

### To free Port
```sudo kill -9 `sudo lsof -t -i:<port no> ```
