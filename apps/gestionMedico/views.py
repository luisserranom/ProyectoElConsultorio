from django.http import HttpResponse
from django.shortcuts import render,redirect
from apps.gestionMedico.models import Especialista,Especialidad
from .forms import EspecialistaForm,EspecialistaEditarForm


from django.contrib import messages
# Create your views here.

def gestionMedico(request): 
    try:
        if request.session['admin_login']['userA']:
            if request.method == "POST":
                rut = request.POST.get('rut_especialista')
                especialistaVerif = Especialista.objects.filter(rut_especialista = rut).exists()
                if especialistaVerif:
                    """ messages.error(request,"Usuario ya creado") """
                    data ={
                        'especialista': Especialista.objects.all(),
                        'especialidad': Especialidad.objects.all(),
                        'form':EspecialistaForm(),
                        'error': True,
                        } 
                    return render(request,'gestionMedico/GestionDoctor.html',data)
                else:
                    form = EspecialistaForm(request.POST or None)
                    if form.is_valid():
                        form.save()
                        return redirect('gestionMedico')
            else:
                data ={
                    'especialista': Especialista.objects.all(),
                    'especialidad': Especialidad.objects.all(),
                    'form':EspecialistaForm()
                }
                return render(request,'gestionMedico/gestionDoctor.html',data)
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')
        


def eliminarMedico(request,rut):
    try:
        if request.session['admin_login']['userA']:
            especialista = Especialista.objects.get(rut_especialista = rut)
            especialista.delete() 
            return redirect('gestionMedico')
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')
        
def editarMedico(request,rut):
    try:
        if request.session['admin_login']['userA']:
            especialista = Especialista.objects.get(rut_especialista = rut)
            if request.method == "POST":
                form = EspecialistaEditarForm(request.POST or None,instance = especialista)
                if form.is_valid():
                    form.save()
                    messages.success(request,"Editado correctamente")
                    return redirect('gestionMedico')
            else:
                data = {
                    'form': EspecialistaEditarForm(instance = especialista)
                } 
                return render(request,'gestionMedico/editar.html',data)
        else:
            request.session.flush()
            return redirect('login')
    except KeyError:
        request.session.flush()
        return redirect('login')