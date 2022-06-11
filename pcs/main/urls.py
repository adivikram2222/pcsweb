from django.contrib import admin
from django.urls import path
from main import views


urlpatterns = [
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("service",views.service,name="service"),
    path("contact",views.contact,name="contact"),
    path("educational",views.educational,name="educational"),
    path("base",views.base,name="base"),
    path("registeration",views.registeration,name="registeration"),
    path("login",views.login,name="login"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("itservices",views.itservices,name="itservices"),
]