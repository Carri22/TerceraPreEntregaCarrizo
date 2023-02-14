from django import forms

class PacienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class MedicoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    especialidad = forms.CharField()