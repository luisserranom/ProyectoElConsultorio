from django.shortcuts import render,redirect
from .models import FichaMedica, Receta, Paciente
# Create your views here.
def homeGestionUsuario(request):  
    try:   
        if request.session['paciente_login']['userP']:
            """ TRAIGO DATOS DE LA SESION """
            rutSession = request.session['paciente_login']['userP']['rut']
            
            paciente = Paciente.objects.get(rut = rutSession)
            
            fichaVer = FichaMedica.objects.filter(id_paciente = paciente).exists()
            if fichaVer:
                ficha = FichaMedica.objects.filter(id_paciente = paciente)
                idRec = []
                if ficha == None:
                        pass
                else:
                    for x in ficha:
                        if x.id_receta == None:
                            pass
                        else:
                            receta = x.id_receta.id_receta
                            idRec.append(receta)
                
                recetas = []
                if idRec == None:
                    recetas = []
                else:
                    for x in idRec:
                        aa = Receta.objects.get(id_receta = x)
                        recetas.append(aa)
                
                
                data={
                    'Receta' : recetas,
                    'ficha' : ficha
                }
                return render(request,'calendario/AgendaMedicamento.html',data)
            else:
                                
                data={
                    'Receta' : False,
                    'ficha' : False
                }
                return render(request,'calendario/AgendaMedicamento.html',data)
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')
        