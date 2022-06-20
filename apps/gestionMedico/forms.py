from django import forms
from .models import Especialista

class EspecialistaForm(forms.ModelForm):
    class Meta:
        model = Especialista
        
        fields = [  
            'rut_especialista',
            'nombre_especialista',
            'apellido_especialista',
            'id_especialidad',
        ]
        labels = {  
            'rut_especialista':'Rut',
            'nombre_especialista':'Nombre',
            'apellido_especialista':'Apellido',
            'id_especialidad':'Especialidad',
        }
        widgets = {
            'rut_especialista': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_especialista': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_especialista': forms.TextInput(attrs={'class':'form-control'}),
            'id_especialidad': forms.Select(attrs={'class':'form-select'}),
        }
      
class EspecialistaEditarForm(forms.ModelForm):
    class Meta:
        model = Especialista
        
        fields = [  
            'rut_especialista',
            'nombre_especialista',
            'apellido_especialista',
            'id_especialidad',
        ]
        labels = {  
            'rut_especialista':'Rut',
            'nombre_especialista':'Nombre',
            'apellido_especialista':'Apellido',
            'id_especialidad':'Especialidad',
        }
        widgets = {
            'rut_especialista': forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
            'nombre_especialista': forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
            'apellido_especialista': forms.TextInput(attrs={'class':'form-control','readonly':'True'}),
            'id_especialidad': forms.Select(attrs={'class':'form-select'}),
        }