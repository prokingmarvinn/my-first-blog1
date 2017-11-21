from django.contrib import admin
from finals.models import Estudiante, EstudianteAdmin, Materia, MateriaAdmin

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Materia, MateriaAdmin)
# Register your models here.
