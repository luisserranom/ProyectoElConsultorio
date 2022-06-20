from email import message
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def homeFarm(request):  
    try:   
        if request.session['farmaceutico_login']['userF']:
            if request.method == 'POST':
                if 'btn-buscar' in request.POST:
                    """ TRAIGO DATOS DE LA SESION """
                    rutSession = request.POST.get('paciente_rut')
                    
                    paciente = Paciente.objects.get(rut = rutSession)
                    if paciente == None:
                        messages.error(request,"error paciente no existe")
                        return render(request,'gestionFarmaceutico/gestFarm.html')
                    fichaVer = FichaMedica.objects.filter(id_paciente = paciente).exists()
                    if fichaVer:
                        ficha = FichaMedica.objects.filter(id_paciente = paciente)
                        print(ficha)
                        idRec = []
                        if ficha == None:
                                print("error ficha")
                        else:
                            for x in ficha:
                                if x.id_receta == None:
                                    print("entre al x.idreceta")
                                else:
                                    receta = x.id_receta.id_receta
                                    idRec.append(receta)
                        print(idRec)
                        
                        recetas = []
                        if idRec == None:
                            recetas = []
                        else:
                            for x in idRec:
                                aa = Receta.objects.get(id_receta = x)
                                recetas.append(aa)
                        print (recetas)
                        
                        data={
                            'Receta' : recetas,
                            'ficha' : ficha
                        }
                        print("no entraste al if de abajo mi")
                        return render(request,'gestionFarmaceutico/gestFarm.html',data)                          
                else:              
                    data={
                        'Receta' : False,
                    }
                    return render(request,'gestionFarmaceutico/gestFarm.html',data)
            else:                    
                data={
                    'Receta' : False,
                    'ficha' : False
                }
                return render(request,'gestionFarmaceutico/gestFarm.html',data)
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')


def modifReceta(request,id):
    try:   
        if request.session['farmaceutico_login']['userF']:
            if request.method == 'POST':
                a = request.POST.get('estado_receta')
                b = request.POST.get('respuesta_receta')  
                print(a)
                print(b)
                receta = Receta.objects.get(id_receta = id)
                receta.estado = a
                receta.respuesta = b  
                receta.save()
                print("entre al if ")
                return redirect('homeFarm')
            else:
                data = {
                    "receta":Receta.objects.get(id_receta = id)
                }
                return render(request,'gestionFarmaceutico/modifReceta.html')
    except KeyError:
        request.session.flush()
        return redirect('login')
