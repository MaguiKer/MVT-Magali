from django.db import models

# Create your models here.
class Personas(models.Model):
    nombre=models.CharField(max_length=100)
    edad=models.IntegerField()
    fechaNacimiento=models.DateField()