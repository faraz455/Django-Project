from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display =  ("service_icon", "service_title", "service_des")
# Register your models here.

admin.site.register(Service,ServiceAdmin)
