from django import urls
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CustomeUserView, UserProfileView

router = DefaultRouter()
router.register('user', CustomeUserView)
router.register('user-profile', UserProfileView)

urlpatterns = [
    path("", include(router.urls))
]
