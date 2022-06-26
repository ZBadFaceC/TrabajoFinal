from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('canchas', canchas, name="canchas"),
    path('clientes', clientes, name="clientes"),
    path('deportes', deportes, name="deportes"),
    path('crear_deportes', crear_deportes, name="crear_deportes"),
    path('crear_canchas', crear_canchas, name="crear_canchas"),
    path('crear_clientes', crear_clientes, name="crear_clientes"),
]