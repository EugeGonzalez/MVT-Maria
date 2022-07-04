from django.db import models

# Create your models here.


class Familia(models.Model):
    integrante= models.CharField(max_length=50)
    nombre= models.CharField(max_length=50)
    fecha_nacimiento= models.DateField()
    