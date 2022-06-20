from django.shortcuts import render,redirect
from .models import Paciente,FichaMedica,Receta,EnfermedadesCronicas,Alergias,EnfermedadesTerminales,Observaciones
# Create your views here.
def homeFicha(request):

    try:
        if request.session['paciente_login']['userP']:
            """ TRAIGO DATOS DE LA SESION """
            rutSession = request.session['paciente_login']['userP']['rut']
            paciente = Paciente.objects.get(rut = rutSession)   
            fichaVer = FichaMedica.objects.filter(id_paciente = paciente).exists()  
            if fichaVer:
                    ficha = FichaMedica.objects.filter(id_paciente = paciente)
                    idRec = []
                    idEnfCro = []
                    idEnfTer = []
                    idAler = []
                    idObser = []
                    if ficha == None:
                        print("error en la ficha")
                    else:
                        for x in ficha:
                            if x.id_receta == None:
                                print("Tiene un campo vacio receta")
                            else:
                                receta = x.id_receta.id_receta
                                idRec.append(receta)
                                
                            if x.id_enfermedades_cronicas == None:
                                print("Tiene un campo vacio")
                            else:                              
                                enfermedadesCronicas = x.id_enfermedades_cronicas.id_enfermedades_cronicas
                                idEnfCro.append(enfermedadesCronicas)   
                                 
                            if x.id_alergias == None:
                                print("Tiene un campo vacio")
                            else:
                                alergia = x.id_alergias.id_alergias
                                idAler.append(alergia)
                                
                            if x.id_enfermedades_terminales == None:
                                print("Tiene un campo vacio")
                            else:
                                enfermedadesTerminales = x.id_enfermedades_terminales.id_enfermedades_terminales
                                idEnfTer.append(enfermedadesTerminales)
                            print("ESTA ES LA ID ")
                            print(x.id_observacion)   
                            if x.id_observacion == None :
                                print("Tiene un campo vacio")
                            else:
                                observacion = x.id_observacion.id_observacion
                                idObser.append(observacion) 
                    
                    recetas = []
                    if idRec == []:
                        print("Campo vacio")
                    else:
                        for x in idRec:
                            recet = Receta.objects.get(id_receta = x)
                            recetas.append(recet)
                    
                    enfermedadesCronic = []
                    if idEnfCro == []:
                        print("Campo vacio")
                    else:
                        for x in idEnfCro:
                            enfCro = EnfermedadesCronicas.objects.get(id_enfermedades_cronicas = x)
                            enfermedadesCronic.append(enfCro)
                    
                    alergias = [None]
                    if idAler == []:
                        print("Campo vacio")
                    else:
                        for x in idAler:
                            aler = Alergias.objects.get(id_alergias = x)
                            alergias.append(aler)
                    
                    enferTerminales = []
                    print(idEnfTer)
                    if idEnfTer == []:
                        print("Campo vacio")
                    else:
                        for x in idEnfTer:
                            enfTer = EnfermedadesTerminales.objects.get(id_enfermedades_terminales = x)
                            enferTerminales.append(enfTer)   
                    
                    observac = []
                    if idObser == []:
                        print("Campo vacio")
                    else:
                        for x in idObser:
                            obs = Observaciones.objects.get(id_observacion = x)
                            observac.append(obs)                                
                    
                            
                    data={
                        'Receta' : recetas,
                        'EnfCronic': enfermedadesCronic,
                        'Alergia' : alergias,
                        'EnfermedadesTerminales':enferTerminales,
                        'Observaciones':observac,
                        'ficha' : ficha
                    }
                    return render(request,'gestionFicha/ficha.html',data)
            else:              
                data={
                    'ficha' : False
                }
                return render(request,'gestionFicha/ficha.html',data)
            
        
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')