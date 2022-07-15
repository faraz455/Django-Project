from django.db import models

# Create your models here.
from tinymce.models import HTMLField

class News(models.Model):
    news_title = models.CharField(max_length=100)
    news_des = HTMLField()