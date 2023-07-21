from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics

#modelo de datos
from .models import Participantes

#serializador
from .serializers import ParticipantesSerial

#funcion based view
from rest_framework import status
# decorador para las funciones
from rest_framework.decorators import api_view
# respuesta de la funcion
from rest_framework.response import Response


#class based view
from rest_framework.views import APIView
from django.http import Http404


#generic class based view
class SnippetList(generics.ListCreateAPIView):
    queryset = Participantes.objects.all()
    serializer_class = ParticipantesSerial


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participantes.objects.all()
    serializer_class = ParticipantesSerial

# Create your views here.

def index(request):
    return render(request, 'index.html')


#sin framework ni serializador
def partipantes(request):
    participantes = Participantes.objects.all()
    data = {'participantes': list(participantes.values())}
    return JsonResponse(data)


#funcion based view

@api_view(['GET', 'POST'])
def listaParticipantes(request):
    if request.method == 'GET':
        participantes = Participantes.objects.all()
        serial = ParticipantesSerial(participantes, many=True)
        return Response(serial.data)

    if request.method == 'POST':
        serial = ParticipantesSerial(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def detalleParticipante(request, pk):
    try:
        participante = Participantes.objects.get(pk=pk)
    except Participantes.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = ParticipantesSerial(participante)
        return Response(serial.data)
    
    if request.method == 'PUT':
        serial = ParticipantesSerial(participante, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        participante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#CLASS BASED VIEW

class ListaParticipantes(APIView):
    def get(self, request):
        participante=Participantes.objects.all()
        serial = ParticipantesSerial(participante, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial = ParticipantesSerial(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

class DestalleParticipante(APIView):
    def get_object(self, pk):
        try:
            return Participantes.objects.get(pk=pk)
        except Participantes.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        try:
            participante = self.get_object(pk)
            serial = ParticipantesSerial(participante)
            return Response(serial.data)
        except Http404:
            return Response({"error": "Participante no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            participante = self.get_object(pk)
            serial = ParticipantesSerial(participante, data=request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data)
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        except Http404:
            return Response({"error": "Participante no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            participante = self.get_object(pk)
            participante.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response({"error": "Participante no encontrado"}, status=status.HTTP_404_NOT_FOUND)