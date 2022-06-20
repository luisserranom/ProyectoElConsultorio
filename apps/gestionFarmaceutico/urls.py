from .views import homeFarm,modifReceta

from django.urls import path

urlpatterns = [
    path('gestFarm/',homeFarm, name = 'homeFarm'),
    path('gestFarm/editar/<int:id>',modifReceta,name="modifcar-receta"),
]