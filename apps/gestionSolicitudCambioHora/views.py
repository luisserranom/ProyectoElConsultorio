from django.shortcuts import redirect, render
from pkg_resources import require
from .models import *

from django.contrib import messages
# Create your views here.
def homeSolic(request):
    if request.method == 'POST':
        pass
    else:
        data = {
            "listaSolic": ListaSolicitudHora.objects.all()
        }
        return render(request,'gestionSolicitudHora/gestSolicHora.html',data)
    
    
def modifHora(request,id):
    if request.method == 'POST':
        estado = request.POST.get("estado")
        respuesta = request.POST.get('respuesta')
        solic = ListaSolicitudHora.objects.get(id_solicitud = id)
        solic.estado = estado
        if estado == "aceptado":
            solic.respuesta = ""
            solic.save()
            registro = solic.id_registro.id_registro
        
            registroI = [registro]
            for x in registroI:
                regis = RegistroHora.objects.get(id_registro = x)
    
            regis.hora = solic.hora
            regis.fecha = solic.fecha
            regis.save()            
            return redirect('homeSolic')  
        elif estado == "rechazado":
            solic.respuesta = respuesta
            solic.save()
            return redirect('homeSolic')
        else:
            messages.error(request,"ERROR")
            return redirect('homeSolic')
    else:
        data = {
            "lista": ListaSolicitudHora.objects.get(id_solicitud=id)
        }
        return render(request,'gestionSolicitudHora/mm.html',data)