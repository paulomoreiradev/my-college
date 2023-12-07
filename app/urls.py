from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("calculadora/", views.calculadora_turno, name="calculadora-turno"),
    path("sobre/", views.sobre, name="sobre-o-curso"),
    path("trilhas/", views.trilhas, name="trilhas"),
    path("sobre-o-projeto/", views.o_projeto, name="sobre-o-projeto"),
    path("calculadora/diurno/obrigatorias", views.ObrigatoriasDiurnoView.as_view(), name="diurno"),
    path("calculadora/noturno/obrigatorias", views.ObrigatoriasNoturnoView.as_view(), name="noturno"),
    path("calculadora/diurno/eletivas", views.EletivasDiurnoView.as_view(), name="eletivas-diurno"),
    path("calculadora/noturno/eletivas", views.EletivasNoturnoView.as_view(), name="eletivas-noturno"),
    path("calculadora/diurno/optativas", views.OptativasDiurnoView.as_view(), name="optativas-diurno"),
    path("calculadora/noturno/optativas", views.OptativasNoturnoView.as_view(), name="optativas-noturno"),
    path("calculadora/diurno/horas-complementares", views.HorasComplementaresDiurnoView.as_view(), name="horas-diurno"),
    path("calculadora/noturno/horas-complementares", views.HorasComplementaresNoturnoView.as_view(), name="horas-noturno"),
    path("calculadora/resultado/<int:pk>/", views.ConclusaoView.as_view(), name="resultado"),
]