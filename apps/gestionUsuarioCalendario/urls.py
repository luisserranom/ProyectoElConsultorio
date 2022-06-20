from .views import homeGestionUsuario

from django.urls import path

urlpatterns = [
    path('calendario/',homeGestionUsuario, name = 'gestionCalendario'),

]