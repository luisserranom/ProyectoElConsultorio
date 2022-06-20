from django.forms import RegexField
from django.shortcuts import render
from .models import *
# Create your views here.
def homeDashboard(request):
    if request.method == 'POST':
        print("plop")
    else:
        rut = "123456789"   """ AGREGAR DE DONDE SACAR ESPECIALISTA """ 
        """ especialista =Especialista.objects.get(rut_especialista = "")  """
    
        """ registroHora = RegistroHora.objects.filter(id_especialista = especialista.id_especialista)
        print(registroHora) """
        """  cantidadPaciente = 0
        for x in registroHora:
            cantidadPaciente= cantidadPaciente + 1 """
        
        
        
        return render(request,'dashboard/Dashboard.html')