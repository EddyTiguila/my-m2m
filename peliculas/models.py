from django.db import models

#Define la clase Actor, esta tabla no se relaciona con nadie más.

class Actor(models.Model):
    nombre  =   models.CharField(max_length=30)
    fecha_nacimiento = models.CharField(max_length=30)
    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    nombre    = models.CharField(max_length=60)
    anio      = models.IntegerField()
    actores   = models.ManyToManyField(Actor, through='Actuacion')
    def __str__(self):
        return self.nombre

class Actuacion (models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
# Create your models here.
