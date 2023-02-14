from django.shortcuts import redirect, render
from AppHospital.models import Medico,Paciente,MedicoInterno
from .forms import MedicoFormulario
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,'AppHospital/padre.html')

def medico(request):
    return render(request,'AppHospital/medico.html')

def medico_formulario(request):
    
    mis_medicos = Medico.objects.all()

    #Aqui recibiremos toda la informacion enviada mediante el formulario
    if request.method == "POST":
        mi_formulario = MedicoFormulario(request.POST)

        #Validamos que los datos correspondan a los esperados
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            medico = Medico(
                nombre = informacion['nombre'],
                apellido=informacion['apellido'],
                especialidad=informacion['especialidad']
                )
            medico.save()
            return redirect('inicio')

    else:
        #Inicializamos un formulario vacio para construir el HTML
        mi_formulario = MedicoFormulario()
    return render(request, 'AppHospital/medico-formulario.html',{'formulario_medico': mi_formulario, 'mis_medicos':mis_medicos})

def busqueda_especialidad(request):
    return render(request, 'AppHospital/busqueda-especialidad.html')

def buscar(request):
    if request.GET["especialidad"]:
        especialidad = request.GET["especialidad"]
        medicos = Medico.objects.filter(especialidad__icontains=especialidad)

        return render(request, 'AppHospital/resultado-busqueda.html',{'medicos': medicos, 'especialidad':especialidad})
    
    else:
        respuesta = f'No se encontro la especialidad:{request.GET["especialidad"]}'
          
    return HttpResponse(respuesta)