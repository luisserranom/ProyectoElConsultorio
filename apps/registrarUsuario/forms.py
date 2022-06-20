from django import forms
from .models import Usuario

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Usuario
        
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
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }