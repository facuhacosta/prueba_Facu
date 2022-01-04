from django.db import models

# Create your models here.

class clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    email=models.EmailField()
    tel=models.CharField(max_length=20)
    
class articulos(models.Model):
    nombre=models.CharField(max_length=20)
    seccion=models.CharField(max_length=30)
    precio=models.IntegerField()
    
class pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entragado=models.BooleanField()
        
    