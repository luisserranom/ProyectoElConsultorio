from django.shortcuts import redirect, render
from .models import *

from django.contrib import messages
# Create your views here.
def homeSolic(request):
    try:
        if request.session['admin_login']['userA']:
            if request.method == 'POST':
                pass
            else:        
                data = {
                    "listaSolic": ListaSolicitudHora.objects.all()
                }
                return render(request,'gestionSolicitudHora/gestSolicHora.html',data) 
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')
    
    
    
def modifHora(request,id):
    try:
        if request.session['admin_login']['userA']:
            if request.method == 'POST':
                estado = request.POST.get("estado")
                respuesta = request.POST.get('respuesta')
                print(estado)
                print(respuesta)
                solic = ListaSolicitudHora.objects.get(id_solicitud = id)
                solic.estado = estado
                if estado.lower() == "aceptado":
                    print("entre al if aceptado")
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
                elif estado.lower() == "rechazado":
                    print("entre al if rechazado")
                    solic.respuesta = respuesta
                    solic.save()
                    return redirect('homeSolic')
                else:
                    print("error")
                    return redirect('homeSolic')
            else:
                data = {
                    "lista": ListaSolicitudHora.objects.get(id_solicitud=id)
                }
                return render(request,'gestionSolicitudHora/modificarHora.html',data)    
            
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')
   
    