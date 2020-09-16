from django.contrib import admin
from django.urls import path, include
from dota2 import views


urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),      
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("support_heroes", views.support_heroes, name='support_heroes'),
    path("carry_heroes", views.carry_heroes, name='carry_heroes'),
]