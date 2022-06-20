from django.urls import URLPattern, path
from .views import homeDashboard

urlpatterns = [
    path('dashboard/',homeDashboard,name="dashboard"),

]