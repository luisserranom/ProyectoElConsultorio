from .views import homeGestionUsuario,eliminarHoraMedica,solicitarCambioHora,agregarHora,gestorHora,estadoSolic

from django.urls import path

urlpatterns = [
    path('tomaHora/',homeGestionUsuario, name = 'tomaHora'),
    path('gestionUsuario/agregar/<int:id>',agregarHora, name = 'agregar-hora-medica'),
    path('gestorHora/',gestorHora,name = 'gestorHora'),
    path('gestorHora/eliminar/<int:id>', eliminarHoraMedica, name = 'eliminar-hora'),
    path('gestionUsuario/solicitar/<int:id>',solicitarCambioHora, name = 'solicitar-hora-medica'),
    path('gestionUsuario/estadoSolicitud',estadoSolic, name = 'estado-solic'),
]