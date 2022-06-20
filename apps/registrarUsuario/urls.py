from django.urls import URLPattern, path
from .views import registrarUsuario

urlpatterns = [   
    path('registrarUsuario',registrarUsuario,name="registrarUsuario"),
    
]