from django.shortcuts import render,redirect
from .models import RegistroHora, ListaSolicitudHora,Hora,Paciente,Especialista,Area,Rango
import datetime
from django.contrib import messages

from datetime import datetime
# Create your views here.

def homeGestionUsuario(request):
    try:
        if request.session['paciente_login']['userP']:
            if request.method == "POST":
                pass
            else:
                rutSession = request.session['paciente_login']['userP']['rut']
                paciente = Paciente.objects.get(rut = rutSession)
                registroHr = RegistroHora.objects.filter(id_paciente = paciente)
                test = 0
                for x in registroHr:
                    test = test + 1
                
                if test >= 2:
                    messages.error(request,"usted ya posee las 2 horas del dia")
                    data = {
                        'error': True,
                    }
                    return render(request,'tomaHora/TomaDeHora.html',data)
                else:
                    fecha = int(datetime.now().strftime(" %d") )
                    hora = int(datetime.now().strftime(" %H") )
                    horasFiltradas = []
                    horasBase= Hora.objects.filter(estado = "disponible")
                    
                    data = {
                        'hora':Hora.objects.filter(estado = "disponible"),
                        'error': False,
                        'area':Area.objects.all(),
                    }
                    return render(request,'tomaHora/TomaDeHora.html',data)
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')

def agregarHora(request,id):
    try:
        if request.session['paciente_login']['userP']:
            if request.method == "POST":
                pass
                print("tas ca")   
            else:
                rutSession = request.session['paciente_login']['userP']['rut']
                paciente = Paciente.objects.get(rut = rutSession)
                horaPc = int(datetime.now().strftime(" %H") )
                print("estas en el else de agregar hora")              
                rangoA = Rango.objects.get(id_rango = 1)
                rangoB = Rango.objects.get(id_rango = 2)
                rangoC = Rango.objects.get(id_rango = 3)
                rangoPaciente = paciente.id_rango
                registroHr = RegistroHora.objects.filter(id_paciente = paciente)
                test = 0
                for x in registroHr:
                    test = test + 1
                if test >= 2:
                    messages.error(request,"usted ya posee las 2 horas del dia")
                    data = {
                        'error': True,
                    }
                    return render(request,'tomaHora/TomaDeHora.html',data)
                else:
                    if rangoA == rangoPaciente:
                        if horaPc == 8:
                            hora = Hora.objects.get(id_hora = id)
                            hora.estado = "no disponible"
                            hora.save() 
                            RegistroHora.objects.create(
                                descripcion = "porque si",
                                fecha =hora.fecha,
                                hora = hora.hora,
                                id_paciente = paciente,
                                id_hora = hora,
                            )
                            data = {
                                'hora': Hora.objects.filter(estado = "disponible"),
                                'error': False,
                            }
                            return render(request,'tomaHora/TomaDeHora.html',data)  
                        else:
                            data = {
                                'hora': Hora.objects.filter(estado = "disponible"),
                                'error': False,
                            }
                            messages.error(request,"NO PUEDES AGREGAR HORA, YA QUE NO TE CORRESPONDE POR TU RANGO A , ESTA DEBE SER A LAS 8AM")
                            return render(request,'tomaHora/TomaDeHora.html',data)  
                        
                    if rangoB == rangoPaciente:
                        if horaPc == 9:
                            hora = Hora.objects.get(id_hora = id)
                            hora.estado = "no disponible"
                            hora.save() 
                            RegistroHora.objects.create(
                                descripcion = "porque si",
                                fecha =hora.fecha,
                                hora = hora.hora,
                                id_paciente = paciente,
                                id_hora = hora,
                            )
                            data = {
                                'hora': Hora.objects.filter(estado = "disponible"),
                                'error': False,
                            }
                            return render(request,'tomaHora/TomaDeHora.html',data)  
                        else:
                            data = {
                                'hora': Hora.objects.filter(estado = "disponible"),
                                'error': False,
                            }
                            messages.error(request,"NO PUEDES AGREGAR HORA, YA QUE NO TE CORRESPONDE POR TU RANGO A , ESTA DEBE SER A LAS 9AM")
                            return render(request,'tomaHora/TomaDeHora.html',data)  
                    if rangoC == rangoPaciente:
                        if horaPc == 10:
                            hora = Hora.objects.get(id_hora = id)
                            hora.estado = "no disponible"
                            hora.save() 
                            RegistroHora.objects.create(
                                descripcion = "porque si",
                                fecha =hora.fecha,
                                hora = hora.hora,
                                id_paciente = paciente,
                                id_hora = hora,
                            )
                            data = {
                                'hora': Hora.objects.filter(estado = "disponible"),
                                'error': False,
                            }
                            return render(request,'tomaHora/TomaDeHora.html',data)  
                        else:
                            data = {
                                'hora': Hora.objects.filter(estado = "disponible"),
                                'error': False,
                            }
                            messages.error(request,"NO PUEDES AGREGAR HORA, YA QUE NO TE CORRESPONDE POR TU RANGO A , ESTA DEBE SER A LAS 10AM")
                            return render(request,'tomaHora/TomaDeHora.html',data)      
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')   
  
def gestorHora(request):
    try:
        if request.session['paciente_login']['userP']:
            if request.method == 'POST':
                print("xd")
            else:
                rutSession = request.session['paciente_login']['userP']['rut']
                paciente = Paciente.objects.get(rut = rutSession)
                registroHr = RegistroHora.objects.filter(id_paciente = paciente)
                listaSolic = []
                for x in registroHr:
                    id_reg = x.id_registro
                    print(id_reg)
                    verSolic = ListaSolicitudHora.objects.filter(id_registro = id_reg).exists()
                    if verSolic:
                        print("entre aca")
                        solicitud = ListaSolicitudHora.objects.get(id_registro = id_reg)
                        listaSolic.append(solicitud)
                    else:
                        print("entre aca al falseee")
                data = {
                    'registro':registroHr,
                    'lista':listaSolic,
                }            
                return render(request,'tomaHora/GestorHora.html',data)
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')

def estadoSolic(request):
    try:
        if request.session['paciente_login']['userP']:
            if request.method == 'POST':
                pass
            else:
                rutSession = request.session['paciente_login']['userP']['rut']
                paciente = Paciente.objects.get(rut = rutSession)
                registroHr = RegistroHora.objects.filter(id_paciente = paciente)
                listaSolic = []
                for x in registroHr:
                    id_reg = x.id_registro
                    verSolic = ListaSolicitudHora.objects.filter(id_registro = id_reg).exists()
                    if verSolic:
                        solicitud = ListaSolicitudHora.objects.get(id_registro = id_reg)
                        listaSolic.append(solicitud)
                    else:
                        pass
                data = {
                    'lista':listaSolic,
                }            
                return render(request,'tomaHora/EstadoSolicitudesPaciente.html',data)
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login') 
  
  
  
    
def eliminarHoraMedica(request,id):
    try:
        if request.session['paciente_login']['userP']:
            registrHr = RegistroHora.objects.get(id_registro = id)
            
            hora = Hora.objects.get(id_hora = registrHr.id_hora.id_hora)
            hora.estado="disponible"
            hora.save()
            registrHr.delete()
            

            return redirect('gestorHora')
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')


def solicitarCambioHora(request,id):
    try:
        if request.session['paciente_login']['userP']:
            if request.method == "POST":
                registro = RegistroHora.objects.get(id_registro = id)
                id_regist =  registro.id_registro
                print(id_regist)
                verifRegistList = ListaSolicitudHora.objects.filter(id_registro = id_regist).exists()
                if verifRegistList:
                    messages.error(request,"YA SE ENCUETRA UNA SOLICITUD")
                    return redirect('gestorHora') 
                else:
                    descripcion = request.POST.get('descripcion')
                    hora = request.POST.get('hora')
                    fecha = request.POST.get('fecha')
                    print(hora)
                    print(fecha)
                    ListaSolicitudHora.objects.create(
                        descripcion = descripcion,
                        hora = hora,
                        fecha = fecha,
                        id_registro = registro,
                        )
                    return redirect('gestorHora')
            else:
                return render(request,'tomaHora/GestorHora.html')
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login') 

