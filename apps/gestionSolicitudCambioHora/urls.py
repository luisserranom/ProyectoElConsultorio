from .views import homeSolic,modifHora

from django.urls import path

urlpatterns = [
    path('gestionSolic/',homeSolic, name = 'homeSolic'),
    path('gestionSolic/modif/<int:id>',modifHora,name="modif-hora"), 
]