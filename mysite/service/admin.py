from django.contrib import admin
from service.models import Service, Blog, Car

class ServiceAdmin(admin.ModelAdmin):
    list_display =  ("service_icon", "service_title", "service_des")
# Register your models here.

admin.site.register(Service,ServiceAdmin)
admin.site.register((Blog,Car,))