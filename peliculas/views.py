from django.shortcuts import render, redirect
from .models import *
from .forms import ActuacionForm
from .forms import ActorForm
from .forms import PeliculaForm

def home (request):
    return render(request, 'index.html')

def crearActuacion(request):
    if request.method =='POST':
        form=ActuacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =ActuacionForm()
        return render(request,'peliculas/crear_actuacion.html', {'form':form})

def crearActor(request):
    if request.method =='POST':
        form=ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =ActorForm()
        return render(request,'peliculas/crear_actor.html', {'form':form})

def crearPelicula(request):
    if request.method =='POST':
        form=PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form =PeliculaForm()
        return render(request,'peliculas/crear_pelicula.html', {'form':form})

# Create your views here.
