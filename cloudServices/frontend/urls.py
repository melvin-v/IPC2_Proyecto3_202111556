from unicodedata import name
from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("enviarconfiguracion/", views.enviarConf, name='enviarConfiguracion'),
    path("enviarconsumo/", views.enviarCons, name='enviarConsumo'),
    path("consultadatos/", views.getDatos, name='enviarConsumo')
    
]