from django.urls import path
from .views import * 

urlpatterns = [
    path('',inicio, name="inicio"), #Esta es nuestra primer vista
    path('medico/',medico, name="medico"),
    path('medico-formulario/',medico_formulario,name="medico-formulario"),
    path('busqueda-especialidad/',busqueda_especialidad,name="busqueda-especialidad"),
    path('buscar/',buscar,name="buscar"),
    # path('leer-medicos/',leer_medicos,name="leer-medicos"),

]