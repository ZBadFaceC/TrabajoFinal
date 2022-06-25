from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    # path('canchas', canchas, name="canchas"),
    # path('clientes', clientes, name="clientes"),
    # path('deportes', deportes, name="deportes"),
]