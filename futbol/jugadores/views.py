from django.shortcuts import render
from django.http import HttpResponse
from jugadores.models import Jugador


def index(request):
    jug = Jugador()
    cursor = jug.consulta()
    contexto = {
        'lista_jugadores': cursor
        }
    return render(request, 'lista_jugadores.html', contexto)

# Create your views here.
