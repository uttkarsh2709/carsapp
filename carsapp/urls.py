from django.contrib import admin
from django.urls import path
from carsapp import views

urlpatterns = [

    path('', views.index,name="home"),
    path('contact', views.contact,name="contact"),
    path('supercars', views.supercars,name="supercars"),
    path('suvcars', views.suvcars,name="suvcars"),
    path('sedancars', views.sedancars,name="sedancars"),
    path('hatchbackcars', views.hatchbackcars,name="hatchbackcars")
]