from django.contrib import admin
from user.models import CustomUser, User_Profile, Address_Global
# Register your models here.

admin.site.register((CustomUser,User_Profile, Address_Global, ))
