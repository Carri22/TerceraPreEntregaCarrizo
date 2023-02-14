from django.shortcuts import redirect, render
from AppHospital.models import Medico,Paciente,MedicoInterno
from .forms import MedicoFormulario, ProfesorFormulario
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,'AppHospital/inicio.html')

def medico(request):
    return render(request,'AppHospital/medico.html')

def medico_formulario(request):
    mis_medico = Medico.objects.all()
    if request.method == "POST":
        mi_formulario = MedicoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            medico = Medico(nombre = informacion['nombre'],especialidad=informacion['apellido'],especialidad=informacion['especialidad'])
            medico.save()

            nuevo_medico = {'nombre':informacion['nombre'],'apellido':informacion['apellido'],'especialidad':informacion['especialidad']}
            return render(request, 'AppHospital/medico.html',{'formulario_medico': mi_formulario, 'nuevo_medico':nuevo_medico,'mis_medico':mis_medico})

    else:
        mi_formulario = MedicoFormulario()

    return render(request, 'AppHospital/medico.html',{'formulario_medico':mi_formulario, 'mis_medico':mis_medico})

def busqueda_especialidad(request):
    return render(request, 'AppHospital/busqueda-especialidad.html')

def buscar_medico(request):
    if request.GET["especialidad"]:
        especialidad = request.GET["especialidad"]
        medicos = Medico.objects.filter(especialidad__icontains=especialidad)

        return render(request, 'AppHospital/resultado-busqueda.html',{'medicos': medicos, 'especialidad':especialidad})
    
    else:
        respuesta = f'No se encontro la especialidad:{request.GET["especialidad"]}'
          
    return HttpResponse(respuesta)