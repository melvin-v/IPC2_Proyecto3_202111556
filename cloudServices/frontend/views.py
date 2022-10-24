from django.shortcuts import render
from django.http import HttpResponse
from .services import Backend
# Create your views here.

def index(request):
    return render(request, "frontend/index.html", {})


def enviarConf(request):
    if request.method == "POST":
        archivo = request.FILES["inputConf"]
        print(archivo)
        resultado = Backend.enviarConfiguracion(archivo)
        
        return render(request, "frontend/enviarConf.html", resultado)
    
    return render(request, "frontend/enviarConf.html", {"msg":"incorrecto"})

def enviarCons(request):
    if request.method == "POST":
        archivo = request.FILES["inputCons"]
        print(archivo)
        resultado = Backend.enviarConsumo(archivo)
        
        return render(request, "frontend/enviarCons.html", resultado)
    
    return render(request, "frontend/enviarCons.html", {"msg":"incorrecto"})