from django.db import models

# Create your models here.

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