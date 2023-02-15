from django.urls import path
from .views import * 

urlpatterns = [
    #Esta es nuestra primer vista
    path('',inicio, name="inicio"), 

    #Rutas relacionadas a medico
    path('medico/',medico, name="medico"),
    path('medico-formulario/',medico_formulario,name="medico-formulario"),
    path('busqueda-especialidad/',busqueda_especialidad,name="busqueda-especialidad"),
    path('buscar/',buscar,name="buscar"),

    #Rutas relacionadas a paciente
    path('paciente/',paciente,name="paciente"),
    path('paciente-formulario/',paciente_formulario, name="paciente-formulario"),
    
    #Rutas relacionadas a medico interno
    path('medico-interno/',medico_interno,name="medico-interno"),
    path('medico-interno-formulario/',medico_interno_formulario, name="medico-interno-formulario"),
   
]