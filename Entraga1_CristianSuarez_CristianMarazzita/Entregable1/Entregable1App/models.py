from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
    
    usuario = models.OneToOneField('auth.User' , on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatar/' , blank=True, null=True)
    
    
class Cancha(models.Model):
    tipo= models.CharField(max_length=20)
    tamaño = models.IntegerField()
    costo = models.FloatField()
    horario = models.TimeField()
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    
class Deporte(models.Model):
    tipo = models.CharField(max_length=30)
    profesor = models.CharField(max_length=30)
    costo = models.FloatField()