from django.shortcuts import render
from django.http import HttpResponse
from .services import Backend
from .services import UploadFileForm
# Create your views here.

def index(request):
    return render(request, "frontend/index.html", {})


def enviarConf(request):
    if request.method == "POST":
        #archivo =  request.POST.get("inputConf")
        archivo = request.FILES["inputConf"]
        print(archivo)
        resultado = Backend.enviarConfiguracion(archivo)
        
        return render(request, "frontend/enviarConf.html", resultado)
    
    return render(request, "frontend/enviarConf.html", {})