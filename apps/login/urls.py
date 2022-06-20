from django.urls import URLPattern, path
from .views import login,logout

urlpatterns = [
    path('login',login,name="login"),
    path('logout/',logout,name='logout'),
]