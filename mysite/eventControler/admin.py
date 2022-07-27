from django.contrib import admin
from .models import EventMain, EventFeature, EventAttender, DogsModel


admin.site.register((EventMain, EventFeature, EventAttender, DogsModel))

# Register your models here.