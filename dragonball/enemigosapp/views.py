from django.shortcuts import render
from django.shortcuts import redirect
from enemigosapp.models import (Enemigo, Sayayin, Enfrentamientos, )
from enemigosapp.forms import (FormEnemigo, FormSayayin, FormEnfrentamientos, )

# Create your views here.
def index(request):
    return render(request, 'enemigosapp/index.html')

def listarEnemigos(request):
    enemigos = Enemigo.objects.all()
    data = {'enemigos' : enemigos}
    return render(request, 'enemigosapp/listarEnemigos.html', data)

def agregarEnemigo(request):
    form = FormEnemigo()
    if request.method == 'POST':
        form = FormEnemigo(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'enemigosapp/agregarEnemigo.html', data)

def eliminarEnemigo(request, id):
    enemigo = Enemigo.objects.get(id = id)
    enemigo.delete()
    return redirect('/listarEnemigos')

def actualizarEnemigo(request,id):
    enemigo = Enemigo.objects.get(id = id)
    form = FormEnemigo(instance=enemigo)
    if request.method == 'POST':
        form = FormEnemigo(request.POST, instance=enemigo)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'enemigosapp/agregarEnemigo.html', data)

def listarSayayines(request):
    sayayines = Sayayin.objects.all()
    data = {'sayayines':sayayines}
    return render(request, 'enemigosapp/listarSayayines.html', data)

def agregarSayayin(request):
    form = FormSayayin()
    if request.method == 'POST':
        form = FormSayayin(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'enemigosapp/agregarSayayin.html', data)

def eliminarSayayin(request, id):
    sayayin = Sayayin.objects.get(id = id)
    sayayin.delete()
    return redirect('/listarSayayines')

def actualizarSayayin(request, id):
    sayayin = Sayayin.objects.get(id = id)
    form = FormSayayin(instance=sayayin)
    if request.method == 'POST':
        form = FormSayayin(request.POST, instance=sayayin)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'enemigosapp/agregarSayayin.html', data)

def listarEnfrentamientos(request):
    enfrentamientos = Enfrentamientos.objects.select_related('sayayin', 'enemigo').all() #esto trae todos los registros de una tabla y por cada registro trae los datos de Sayayin o Enemigos
    data = {'enfrentamientos': enfrentamientos}
    return render(request, 'enemigosapp/listarEnfrentamientos.html', data)

def agregarEnfrentamiento(request):
    form = FormEnfrentamientos()
    if request.method == 'POST':
        form = FormEnfrentamientos(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'enemigosapp/agregarEnfrentamiento.html', data)

def eliminarEnfrentamiento(request, id):
    enfrentamiento = Enfrentamientos.objects.get(id = id)
    enfrentamiento.delete()
    return redirect('/listarEnfrentamientos')

def actualizarEnfrentamiento(request, id):
    enfrentamiento = Enfrentamientos.objects.get(id = id)
    form = FormEnfrentamientos(instance=enfrentamiento)
    if request.method ==  'POST':
        form = FormEnfrentamientos(request.POST, instance=enfrentamiento)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'enemigosapp/agregarEnfrentamiento.html', data)