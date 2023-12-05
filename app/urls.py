from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("calculadora/", views.calculadora_turno, name="calculadora-turno"),
    path("sobre/", views.sobre, name="sobre-o-curso"),
    path("trilhas/", views.trilhas, name="trilhas"),
    path("sobre-o-projeto/", views.o_projeto, name="sobre-o-projeto"),
    path("calculadora/diurno/", views.obrigatorias_diurno, name="diurno"),
    path("calculadora/noturno/obrigatorias", views.ObrigatoriasNoturnoView.as_view(), name="noturno"),
    path("calculadora/noturno/eletivas", views.EletivasView.as_view(), name="eletivas"),
    path("calculadora/noturno/optativas", views.OptativasView.as_view(), name="optativas"),
]