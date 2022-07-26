from django import urls
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CustomeUserView, User_ProfileView

router = DefaultRouter()
router.register('user', CustomeUserView)
router.register('user-profile', User_ProfileView)

urlpatterns = [
    path("", include(router.urls))
]
