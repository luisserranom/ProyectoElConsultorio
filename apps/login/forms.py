from django import forms
from .models import  UsuarioLogin
from django.forms import ValidationError


class LoginUsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioLogin
        
        fields = [  
            'usuario',
            'password',
        ]
        labels = {  
            'usuario':'usuario',
            'password':'password',
        }
        widgets = {
            'usuario': forms.TextInput(attrs={'class':'form-control','placeholder':'Usuario'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        }