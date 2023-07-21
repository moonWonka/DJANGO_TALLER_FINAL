# serializers.py
from rest_framework import serializers
from .models import Participantes

class ParticipantesSerial(serializers.ModelSerializer):
    class Meta:
        model = Participantes
        fields = ['id', 'nombre', 'telefono', 'fecha_inscripcion', 'institucion', 'hora_inscripcion', 'estado', 'observacion']
