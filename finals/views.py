from django.shortcuts import render
from django.contrib import messages
from .forms import MateriaForm
from finals.models import Materia, Asignacion
# Create your views here.
def pelicula_nueva(request):
    if request.method == "POST":
        formulario = MateriaForm(request.POST)
        if formulario.is_valid():
            asignacion = Materia.objects.create(nombre=formulario.cleaned_data['nombre'], profesor = formulario.cleaned_data['edad'])
            for estudiante_id in request.POST.getlist('materias'):
                asignacion = Asignacion(estudiante_id=estudiante_id, asignacion_id = asignacion.id), Asignacion(materia_id=materia_id,asignacion_id = asignacion.id)
                asignacion.save()
            messages.add_message(request, messages.SUCCESS, 'asignacion Guardado Exitosamente')
    else:
        formulario = MateriaForm()
    return render(request, 'final/final_editar.html', {'formulario': formulario})
#        formulario = MateriaForm(request.POST)
#        if formulario.is_valid():
