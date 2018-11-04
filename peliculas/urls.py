from django.conf.urls import url
from .views import *
urlpatterns =[
url(r'^$',home, name ="index"),
url(r'^crear_actuacion/',crearActuacion, name ="CrearActuacion"),
url(r'^crear_actor/',crearActor, name ="CrearActor"),
url(r'^crear_pelicula/',crearPelicula, name ="CrearPelicula"),
]
