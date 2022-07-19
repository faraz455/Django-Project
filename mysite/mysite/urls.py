"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite import views
from rest_framework.routers import DefaultRouter

# Defaults route create for NewsViewSet that are included ahead of a path
router = DefaultRouter()
router.register('news-viewset',views.NewsViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('', views.homePage, name='homePage'),
    path('course/', views.course, name='course'),
    path('course/<int:courseid>', views.courseDetail, name='courseDetail'),
    path('userform/', views.userform, name='userform'),
    path('submitform/', views.submitform, name='submitform'),
    path('calculator/', views.calculator, name='calculator'),
    path('aboutus/',views.aboutus),
    path('newsdetail/<newsid>', views.detailPage, name='detailPage'),
    path('news/',views.NewsClass.as_view(), name = 'service'),
    path('news/<int:id>',views.NewsClass.as_view()),
    path('news-generics/',views.NewsGenerics.as_view()),
    path('news-generics/<int:id>',views.NewsGenericsUpdate.as_view()),
]
