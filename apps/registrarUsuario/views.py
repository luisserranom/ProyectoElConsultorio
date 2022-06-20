from django.shortcuts import redirect, render
from .models import UsuarioLogin, Paciente,TipoUsuario, FichaMedica
from django.contrib import messages

# Create your views here.
def registrarUsuario(request):
    try:
        if (request.session.session_key == None ):
            if request.method == "POST":
                rut = request.POST.get('rut')
                Papellido = request.POST.get('apellido1')
                Sapellido = request.POST.get('apellido2')
                nombre = request.POST.get('nombre')
                correo = request.POST.get('correo')
                psw1 = request.POST.get('contrasena')
                psw2 = request.POST.get('Rcontrasena')
                veriUsuario = Paciente.objects.filter(rut = rut).exists()
                if psw1 == psw2:
                    
                    Paciente.objects.create(
                        nombre  = nombre,
                        Papellido =Papellido,
                        Sapellido =Sapellido ,
                        rut = rut,
                        correo = correo,
                    )
                    FichaMedica.objects.create(
                        id_receta=None,
                        id_enfermedades_cronicas=None,
                        id_enfermedades_terminales=None,
                        id_observacion =None,
                        id_paciente = Paciente.objects.get(rut = rut)
                    )
                    
                    tipo_usuario = TipoUsuario.objects.get(id_tipo = 1)
                
                    UsuarioLogin.objects.create(
                        usuario = rut,
                        password = psw1,
                        id_paciente =  Paciente.objects.get(rut = rut),
                        id_tipo = tipo_usuario,
                    )
                    data ={
                        'error':False,
                        'verificado':True
                    }
                    messages.success(request,"Felicitaciones, usuario registrado",data)                       
                    return render(request,'core/home.html',data)   
                else:    
                    data={
                        'error':"LAS CONTRASEÑAS NO SON IGUALES"
                    }
                    messages.error(request,"Contraseñas ingresadas no son iguales")
                    return render(request,'registrarUsuario/registrarUsuario.html',data)                         
            else:  
                data = {
                    'error':False
                }  
                return render(request,'registrarUsuario/registrarUsuario.html',data)
        else:
            return redirect ('home')
    except KeyError:
        print("Se ha muerto todo, llamar al Rorro")
        return redirect ('home')

        