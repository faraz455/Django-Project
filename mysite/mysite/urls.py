from django.contrib import admin
from django.urls import path, include
from mysite import views
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

# Defaults route create for NewsViewSet that are included ahead of a path
router = DefaultRouter()
router.register('news-viewset',views.NewsViewSet)

urlpatterns = [
    path('news/',include(router.urls)), 
    path('admin/', admin.site.urls),
    path('gateway/', include("gateway.urls")),
    path('eventControler/', include("eventControler.urls")),
    path('user-main/', include('user.urls')),
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
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # static added as it is use to display the user profile

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls))
    ] + urlpatterns