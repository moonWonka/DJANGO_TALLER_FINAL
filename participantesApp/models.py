from django.db import models

# Create your models here.

class Participantes(models.Model):
    id = models.AutoField(primary_key=True) #primary_key=True es para que sea la llave primaria y autoincrementable
    nombre = models.CharField(max_length=100)
    telefono = models.IntegerField()
    fecha_inscripcion = models.DateField()
    institucion = models.CharField(max_length=100)
    hora_inscripcion = models.DateTimeField(auto_now_add=True) #añade la hora de creacion del registro automaticamente
    estado = models.CharField(max_length=15)
    observacion = models.CharField(max_length=100, blank=True, null=True)

def __str__(self):
    return self.nombre + ' ' + str(self.hora_inscripcion)
