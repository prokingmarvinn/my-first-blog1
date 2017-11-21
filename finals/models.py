from django.db import models
from django.contrib import admin
# Create your models here.
class Estudiante(models.Model):

    nombre  =   models.CharField(max_length=30)
    edad      = models.IntegerField()

    def __str__(self):

        return self.nombre

#class Profesor(models.Model):
#
#    nombre  =   models.CharField(max_length=30)
#    edad      = models.IntegerField()
#
#    def __str__(self):
#
#        return self.nombre
class Materia(models.Model):

    nombre    = models.CharField(max_length=60)
    profesor    = models.CharField(max_length=60)
    CURSOS   = models.ManyToManyField(Estudiante, through='Asignacion')
    def __str__(self):
        return self.nombre

#class Grado(models.Model):

#    nombre    = models.CharField(max_length=60)
#    materia   = models.ManyToManyField(Pasciente, through='Asignacion')
#    def __str__(self):
#        return self.nombre

class Asignacion(models.Model):
    nota     = models.IntegerField()
    Estudiante= models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
#    Grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

class AsignacionInLine(admin.TabularInline):

    model = Asignacion
#muestra un campo extra al momento de insertar, como indicación que se pueden ingresar N actores.
    extra = 1


class EstudianteAdmin(admin.ModelAdmin):
    inlines = (AsignacionInLine,)

class MateriaAdmin (admin.ModelAdmin):
    inlines = (AsignacionInLine,)
