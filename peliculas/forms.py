from django import forms
from .models import *

class ActuacionForm(forms.ModelForm):
    class Meta:
        model =Actuacion
        fields = ['actor','pelicula',]
class ActorForm(forms.ModelForm):
    class Meta:
        model =Actor
        fields = ['nombre','fecha_nacimiento',]

class PeliculaForm(forms.ModelForm):
    class Meta:
        model =Pelicula
        fields = ['nombre','anio',]
