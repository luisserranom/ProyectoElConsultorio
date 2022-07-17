from django.urls import URLPattern, path
from .views import homeDashboard,cargarDatosDash

urlpatterns = [
    path('dashboard/',homeDashboard,name="dashboard"),
    path('dashboard/datos/<int:id>',cargarDatosDash,name="datos-dash"),

]