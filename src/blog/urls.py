from django.urls import path

from src.blog import views

urlpatterns = [
    path('', views.home, name= "home"),
]