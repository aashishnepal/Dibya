from django.urls import path,include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('home', views.home, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('about', views.about, name='about'),
    path('addrecord', views.addrecord, name='addrecord'),
    path('viewrecord', views.viewrecord, name='viewrecord'),
    path('findrecord', views.findrecord, name='findrecord'),
    path('logout', views.login, name='login'),
]