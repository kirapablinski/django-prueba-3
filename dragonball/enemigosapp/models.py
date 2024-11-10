from django.db import models

class Enemigo(models.Model):
    nombre = models.CharField(max_length=50)
    nivel_de_poder = models.IntegerField(default=0)
    asesinatos = models.IntegerField(default=0)
    veces_que_ha_muerto = models.IntegerField(default=0)
    raza = models.CharField(max_length=50)
    organizacion = models.CharField(max_length=50)
    planetas_destruidos = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
    
class Sayayin(models.Model):
    nombre = models.CharField(max_length=50)
    nivel_de_poder = models.IntegerField(default=0)
    veces_ha_resucitado = models.IntegerField(default=0)
    torneos_ganados = models.IntegerField(default=0)
    edad = models.IntegerField(default=0)
    maestro = models.CharField(max_length=50)
    transformacion_max = models.CharField(max_length=50)
    descripcion_breve = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Enfrentamientos(models.Model):
    RESULTADO_OPCIONES = [
        ('gana sayayin', 'Gana Sayayin'),
        ('gana enemigo', 'Gana Enemigo'),
        ('empate', 'Empate'),]

    resultado = models.CharField(max_length=15, choices=RESULTADO_OPCIONES, default='ganado')
    ubicacion = models.CharField(max_length=30)
    saga = models.CharField(max_length=50)
    sayayin = models.ForeignKey(Sayayin, on_delete=models.CASCADE, related_name='enfrentamientos')
    enemigo = models.ForeignKey(Enemigo, on_delete=models.CASCADE, related_name='enfrentamientos')