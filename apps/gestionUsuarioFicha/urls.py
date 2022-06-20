from django.urls import URLPattern, path
from .views import homeFicha

urlpatterns = [
    path('ficha/',homeFicha,name="Ficha"),

]