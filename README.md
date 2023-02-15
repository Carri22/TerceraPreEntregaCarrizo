Hola, presento mi 3ra pre entrega del cuso de python-coder.

El proyecto consta de 3 modelos: Medico,Paciente y MedicoInterno

Una vez clonado el proyecto, debera abrirlo y ejecutar el comando en la terminar de vs code "python manage.py runserver" y ya estara listo para testearlo,
el unico requisito para ejecutar el programa es tener instalado django.

El repositorio cuenta con una base de datos sqlite la cual posee unos pocos registros por cada tabla para poder visualizar registros ya creados en forma de lista dentro de una de las vistas, asi a su vez no debera hacer una migracion

Para acceder a las funciones una vez ejecutado el programa puede acceder atravez del nav/header que se ve a primera vista el cual redirecciona a las vista de Medico, Paciente y Medico interno. Cada una de estas vistas poseen botones que redireccionan a las vistas de los formularios para crear nuevos medicos, pacientes o medicos internos.

La vista de medico tambien posee un boton que redirecciona a un "buscador" de medicos a travez de campo especialidad, debera ingresar un especialidad y el programa mostrara una lista de los medicos cuales posean esa especialidad,
con la excepcion de que no exista medicos con esa especialida o que se haya ingresado una especialida que exista pero que el medico que la posea tenga en su campo registro la especialida con algun cambio ortografico, ejemplo: si existe un medico con la especialidad "Cardiologia" y usted busca "cardiologia" o "Cardiologo" no lo encontrara ya que no es identica a la especialidad que posee el medico existente

En las vistas de los furmularios tambien aparece una lista con los registros existente en la base de datos correspondiente al que vaya a crear. Si crea un nuevo Medico, Paciente o Medico Interno, este aparecera en la lista.


Otra forma de acceder a las vistas es atravez de las urls: 

Para la vistas relacionadas a Medico copiar luego de la urls del inicio :

1 vista principal de medico ----> /medico

2 vista de formulario de medico -----> /medico-formulario

3 vista de busqueda de medicos por especialidad ------> /busqueda-especialidad

Para la vistas relacionadas a Paciente copiar luego de la urls del inicio :

1 vista principal de paciente ----> /paciente

2 vista de formulario de paciente -----> /paciente-formulario

Para la vistas relacionadas a Medico Interno copiar luego de la urls del inicio :

1 vista principal de medico interno ----> /medico-interno

2 vista de formulario de medico interno -----> /medico-interno-formulario







