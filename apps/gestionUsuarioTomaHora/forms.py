from django import forms
from .models import RegistroHora,ListaSolicitudHora
     
class SolicitarCambioHoraform(forms.ModelForm):
    class Meta:
        model = ListaSolicitudHora
        
        fields = [  
            'descripcion',
            'horaSolicitud',
        ]
        labels = {  
            'descripcion':'descripcion',
            'horaSolicitud':'horaSolicitud',
        }
        widgets = {
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'horaSolicitud':forms.TextInput(attrs={'type':'datetime-local'}),
        }