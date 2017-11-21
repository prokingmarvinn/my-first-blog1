from django import forms

from .models import Materia, Estudiante


class MateriaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Materia
        fields = ('nombre', 'profesor', 'CURSOS')
def __init__ (self, *args, **kwargs):
        super(MateriaForm, self).__init__(*args, **kwargs)
        self.fields["cursos"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["cursos"].help_text = "Ingrese los cursos que participaron en la película"
        self.fields["cursos"].queryset = Actor.objects.all()
