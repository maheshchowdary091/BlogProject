from django.contrib import admin
from django.urls import path

from blogpage.views import home
from . import views

urlpatterns = [
    path('', views.home, name = 'blogpage1'),
    path('about/', views.about, name = 'about'),
]