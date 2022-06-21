from django.shortcuts import render,redirect

from .forms import LoginUsuarioForm
from .models import UsuarioLogin,Paciente,TipoUsuario, Administrador,Farmaceutico
from django.contrib import messages


def login(request):
    try:
        if (request.session.session_key == None ):
            if request.method == "POST":
                form = LoginUsuarioForm(request.POST or None)
                if form.is_valid():
                    usuario = request.POST.get('usuario')
                    password = request.POST.get('password')
                    user_paciente = TipoUsuario.objects.get(id_tipo = 1)
                    administrado_us = TipoUsuario.objects.get(id_tipo = 2)
                    farmaceutico_us = TipoUsuario.objects.get(id_tipo = 3)
                    
                    verfUser = UsuarioLogin.objects.filter(usuario = usuario,password = password).exists()
                    if verfUser == True:
                        userLogeado = UsuarioLogin.objects.get(usuario = usuario)
                        if userLogeado.id_tipo == user_paciente:
                            paciente = Paciente.objects.get(rut = usuario)
                            request.session['paciente_login']={'userP':{'nombre':paciente.nombre,'apellido1':paciente.Papellido,'apellido2':paciente.Sapellido,'rut':paciente.rut}}
                            print ("ob 1")
                            data ={
                                'error':False,
                                'verificado':True
                            }
                            """ messages.success(request,"Se a logeado correctamente. "+ request.session.paciente_login.userP.nombe)   """                   
                            return render(request,'core/home.html',data)
                        elif userLogeado.id_tipo == administrado_us:
                            admin = Administrador.objects.get(rut = usuario)
                            request.session['admin_login']={'userA':{'nombre':admin.nombre,'apellido1':admin.Papellido,'apellido2':admin.Sapellido,'rut':admin.rut}}
                            print ("ob2")
                            data ={
                                'error':False,
                                'verificado':True
                            }                 
                            return render(request,'core/home.html',data)
                        elif userLogeado.id_tipo == farmaceutico_us:
                            farmaceutico = Farmaceutico.objects.get(rut = usuario)
                            request.session['farmaceutico_login']={'userF':{'nombre':farmaceutico.nombre,'apellido1':farmaceutico.Papellido,
                                                                            'apellido2':farmaceutico.Sapellido,'rut':farmaceutico.rut}}
                            print ("ob3")
                            data ={
                                'error':False,
                                'verificado':True
                            }                 
                            return render(request,'core/home.html',data)
                        else:
                            """ messages.error(request,"Usuario o contraseña invalidos") """
                            data = {
                                'form':LoginUsuarioForm(),
                                'error':'Usuario o contraseña invalidos'
                                }
                            return render(request,'registration/login.html',data)
                    else:
                        """ messages.error(request,"Error al ingresar sus datos, intentelo nuevamente") """
                        data = {
                            'form':LoginUsuarioForm(),
                            'error':'Error al ingresar sus datos, intentelo nuevamente'
                            }
                        return render(request,'registration/login.html',data)
                else:
                    data = {
                        'form':LoginUsuarioForm(),
                        }
                    return render(request,'registration/login.html',data)
            else:
                data = {'form':LoginUsuarioForm()}
                return render(request,'registration/login.html',data)
        else:
            return redirect ('home')
    except KeyError:
        print("Se ha muerto todo, llamar al Rorro")
        return redirect ('home')
    
def logout(request):
    try:
        request.session.flush()
    except KeyError:
        pass
    return redirect('home')