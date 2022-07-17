from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('login', login_request, name="login"),
    path('register', register_request, name="register"),
    path('logout', logout_request, name="logout"),
    
    path('canchas', canchas, name="canchas"),
    path('crear_canchas', crear_canchas, name="crear_canchas"),
    path('eliminar_cancha/<cancha_id>', eliminar_cancha, name="eliminar_cancha"),
    path('editar_cancha/<cancha_id>', editar_cancha, name="editar_cancha"),
    
    path('clientes', clientes, name="clientes"),
    path('crear_clientes', crear_clientes, name="crear_clientes"),
    path('eliminar_cliente/<cliente_id>', eliminar_cliente, name="eliminar_cliente"),
    path('editar_cliente/<cliente_id>', editar_cliente, name="editar_cliente"),
    
    path('deportes', deportes, name="deportes"),
    path('crear_deportes', crear_deportes, name="crear_deportes"),
    path('eliminar_deporte/<deporte_id>', eliminar_deporte, name="eliminar_deporte"),
    path('editar_deporte/<deporte_id>', editar_deporte, name="editar_deporte"),
]