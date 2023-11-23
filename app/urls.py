from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sobre/", views.sobre, name="sobre"),
    path("trilhas/", views.trilhas, name="trilhas"),
    path("sobre-o-projeto/", views.o_projeto, name="sobre-o-projeto"),
]