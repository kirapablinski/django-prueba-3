from django.contrib import admin
from enemigosapp.models import (Enemigo, Sayayin, Enfrentamientos)

lista_admin = [Enemigo, Sayayin, Enfrentamientos]
class EnemigoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nivel_de_poder', 'asesinatos', 'veces_que_ha_muerto', 'raza', 'organizacion', 'planetas_destruidos']

class SayayinAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nivel_de_poder', 'veces_ha_resucitado', 'torneos_ganados', 'edad', 'maestro', 'transformacion_max', 'descripcion_breve']

class EnfrentamientosAdmin(admin.ModelAdmin):
    list_display = ['resultado', 'ubicacion', 'saga', 'sayayin', 'enemigo']

# Register your models here.
admin.site.register(lista_admin)