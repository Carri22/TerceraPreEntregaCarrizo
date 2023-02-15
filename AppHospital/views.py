from django.shortcuts import redirect, render
from AppHospital.models import Medico,Paciente,MedicoInterno
from .forms import MedicoFormulario,PacienteFormulario,MedicoInternoFormulario
from django.http import HttpResponse

#INICIO
def inicio(request):
    #Retorna a la vista padre-inicio
    return render(request,'AppHospital/padre.html')


#FUNCIONES DE MEDICO
def medico(request):
    #retorna a la vista medico
    return render(request,'AppHospital/medico.html')

def medico_formulario(request):

    #almacena en la variable todos los medicos registrados 
    mis_medicos = Medico.objects.all()

    #Aqui recibiremos toda la informacion enviada mediante el formulario
    if request.method == "POST":
        mi_formulario = MedicoFormulario(request.POST)

        #Validamos que los datos correspondan a los esperados
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            #Crea un objeto medico con la informacion
            medico = Medico(
                nombre = informacion['nombre'],
                apellido=informacion['apellido'],
                especialidad=informacion['especialidad']
                )
            #Guarda el objeto en la base de datos 
            medico.save()
            #vuelve a redireccionar a la vista del formulario para poder seguir registrando medicos
            return redirect('medico-formulario')

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


#FUNCIONES DE PACIENTE
def paciente(request):
    #retorna a la vista paciente
    return render(request,'AppHospital/paciente.html')

def paciente_formulario(request):

    #almacena en la variable todos los pacientes registrados 
    mis_pacientes = Paciente.objects.all()

    #Aqui recibiremos toda la informacion enviada mediante el formulario
    if request.method == "POST":
        mi_formulario = PacienteFormulario(request.POST)

        #Validamos que los datos correspondan a los esperados
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            #Crea el objeto paciente con la informacion
            paciente = Paciente(
                nombre = informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email']
                )
            #guarda el objeto en la base de datos
            paciente.save()
            #vuelve a redireccionar a la vista del formulario para poder seguir registrando medicos
            return redirect('paciente-formulario')

    else:
        #Inicializamos un formulario vacio para construir el HTML
        mi_formulario = PacienteFormulario()
    return render(request, 'AppHospital/paciente-formulario.html',{'formulario_paciente': mi_formulario, 'mis_pacientes':mis_pacientes})


#FUNCIONES DE INTERNO
def medico_interno(request):
    #retorna a la vista medico_interno
    return render(request,'AppHospital/medico-interno.html')

def medico_interno_formulario(request):

    #almacena en la variable todos los medico_internos registrados 
    mis_medico_internos = MedicoInterno.objects.all()

    #Aqui recibiremos toda la informacion enviada mediante el formulario
    if request.method == "POST":
        mi_formulario = MedicoInternoFormulario(request.POST)

        #Validamos que los datos correspondan a los esperados
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            #Crea el objeto medico interno con la informacion
            medico_interno = MedicoInterno(
                nombre = informacion['nombre'],
                apellido=informacion['apellido'],
                facultad=informacion['facultad']
                )
            #guarda el objeto en la base de datos
            medico_interno.save()
            #vuelve a redireccionar a la vista del formulario para poder seguir registrando medicos
            return redirect('medico-interno-formulario')

    else:
        #Inicializamos un formulario vacio para construir el HTML
        mi_formulario = MedicoInternoFormulario()
    return render(request, 'AppHospital/medico-interno-formulario.html',{'formulario_medico_interno': mi_formulario, 'mis_medico_internos':mis_medico_internos})
