from django.shortcuts import render
from django.http import HttpResponse
from .services import Consumo
# Create your views here.

def index(request):
    return render(request, "frontend/index.html", {})

def enviarConf(request):
    if request.method == "POST":
        archivo = request.POST.get("inputConf")
        resultado = Consumo.Backend(archivo)
        
    return render(request, "frontend/enviarConf.html", resultado)
