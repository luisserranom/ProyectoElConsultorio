from dataclasses import dataclass
import json
from django.forms import RegexField
from django.http import JsonResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def homeDashboard(request):
    if request.method == 'POST':
        pass
    else:
        data={
        'especialista' :Especialista.objects.all() 
        }
             
        return render(request,'dashboard/Dashboard.html',data)
    
def cargarDatosDash(request,id):
    print(id)
    if request.method == 'POST':
        pass
    else:
        registroHora = Hora.objects.filter(id_especialista = id)
        print(registroHora) 
        cantidadPaciente = 0
        for x in registroHora:
            cantidadPaciente= cantidadPaciente + 1 
        
        data={
            'especialista' :Especialista.objects.all(),
            'countPaciente':cantidadPaciente
        }
        return render(request,'dashboard/Dashboard.html',data)