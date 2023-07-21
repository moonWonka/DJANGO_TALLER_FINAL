from django.urls import path
from django.contrib import admin
from participantesApp.views import index, partipantes
from participantesApp.views import listaParticipantes, detalleParticipante
from participantesApp.views import ListaParticipantes, DestalleParticipante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('participantes/', partipantes),
    path('participantesFuncion/', listaParticipantes),
    path('participantesFuncion/<int:pk>/', detalleParticipante),
    path('participantesClase/', ListaParticipantes.as_view()),
    path('participantesClase/<int:pk>/', DestalleParticipante.as_view()),
]
