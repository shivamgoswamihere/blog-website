from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),

]