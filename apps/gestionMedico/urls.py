from django.urls import URLPattern, path
from .views import eliminarMedico, gestionMedico,editarMedico
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('gestionMedico/',gestionMedico,name="gestionMedico"),
    path('eliminar-medico/<str:rut>',eliminarMedico,name="eliminar-medico"),
    path('gestionMedico/editar/<str:rut>',editarMedico,name="editar"), 
]