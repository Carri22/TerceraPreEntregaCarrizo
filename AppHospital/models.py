from django.db import models

# Create your models here.
class MedicoInterno(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    facultad = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre + ' '+ str(self.apellido)

class Paciente(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre + self.apellido 

class Medico(models.Model):
  
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.nombre +" "+self.apellido 
