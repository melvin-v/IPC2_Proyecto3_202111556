from unicodedata import name
from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("enviarconfiguracion/", views.enviarConf, name='enviarConfiguracion'),
    path("enviarconsumo/", views.enviarCons, name='enviarConsumo'),
    path("consultadatos/", views.getDatos, name='enviarConsumo'),
    path("creaciondatos/", views.creacionDatos, name='creacionDatos'),
    path("creacionrecursos/", views.creacionRecursos, name='creacionRecursos'),
    path("creacioncategoria/", views.creacionCategoria, name='creacionCategoria'),
    path("creacionconfiguraciones/", views.creacionConfiguraciones, name='creacionConf'),
    path("creacionrecursosub/", views.creacionRescursoSub, name='creacionRec'),
    path("creacioncliente/", views.creacionCliente, name='creacionCliente'),
    path("creacioninstancia/", views.creacionInstancia, name='creacionInstancia'),
    path("facturar/", views.facturar, name='factura'),
    path("reportes/", views.reportes, name='reportes'),
    path("facturapdf/", views.facturarpdf, name='facturapdf')
    
]