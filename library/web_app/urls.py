from django.urls import path
from .views import views_r
from .views import views_a
from .views import views_m
from .views import views_s

urlpatterns = [
    path('', views_r.home, name = 'lib-home'),
    path('about', views_r.library, name = 'lib-about')
]