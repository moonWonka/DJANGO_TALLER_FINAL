from django.contrib import admin
from participantesApp.models import Participantes

# Register your models here.

class ParticipanteAdmin(admin.ModelAdmin):
    
    list_display = ['nombre', 'hora_inscripcion', 'estado', 'observacion']

admin.site.register(Participantes, ParticipanteAdmin)