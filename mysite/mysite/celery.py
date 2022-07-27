from celery import Celery
import os
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()
