from email import message
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def homeFarm(request):  
    try:   
        if request.session['farmaceutico_login']['userF']:
            if request.method == 'POST':
                rutSession = request.POST.get('paciente_rut')
                pacienteVer = Paciente.objects.filter(rut = rutSession).exists()
                if pacienteVer:
                    paciente = Paciente.objects.get(rut = rutSession)
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
                        messages.error(request,"no se encuentra el paciente vuelva a ingresarlo")
                        data={
                        'Receta' : False,
                        'ficha' : False
                        }
                        return render(request,'gestionFarmaceutico/gestFarm.html',data)             
                        
                
                else:
                    data={
                        'Receta' : False,
                        'ficha' : False
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
                return render(request,'gestionFarmaceutico/modifReceta.html')
    except KeyError:
        request.session.flush()
        return redirect('login')
