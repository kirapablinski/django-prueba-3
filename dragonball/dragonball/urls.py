
from django.contrib import admin
from django.urls import path, include
from enemigosapp.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('listarEnemigos/', listarEnemigos),
    path('agregarEnemigo/', agregarEnemigo),
    path('eliminarEnemigo/<int:id>', eliminarEnemigo),
    path('actualizarEnemigo/<int:id>', actualizarEnemigo),
    path('listarSayayines/', listarSayayines),
    path('agregarSayayin/', agregarSayayin),
    path('eliminarSayayin/<int:id>', eliminarSayayin),
    path('actualizarSayayin/<int:id>', actualizarSayayin),
    path('listarEnfrentamientos/', listarEnfrentamientos),
    path('agregarEnfrentamiento/', agregarEnfrentamiento),
    path('actualizarEnfrentamiento/<int:id>', actualizarEnfrentamiento),
    path('eliminarEnfrentamiento/<int:id>', eliminarEnfrentamiento),
    path('api/', include('api.urls')),
    
]
