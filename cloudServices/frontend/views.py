from django.shortcuts import render
from django.http import HttpResponse
from .services import Backend
# Create your views here.

def index(request):
    return render(request, "frontend/index.html", {})


def enviarConf(request):
    if request.method == "POST":
        archivo = request.FILES["inputConf"]
        resultado = Backend.enviarConfiguracion(archivo)
        
        return render(request, "frontend/enviarConf.html", resultado)
    
    return render(request, "frontend/enviarConf.html", {"msg":"incorrecto"})

def enviarCons(request):
    if request.method == "POST":
        archivo = request.FILES["inputCons"]
        resultado = Backend.enviarConsumo(archivo)
        
        return render(request, "frontend/enviarCons.html", resultado)
    
    return render(request, "frontend/enviarCons.html", {"msg":"incorrecto"})

def getDatos(request):
    datos = Backend.getDatos()
    return render(request, "frontend/consultaDatos.html", datos)

def creacionDatos(request):
    return render(request, "frontend/creacionDatos.html", {})

def creacionRecursos(request):
    if request.method == "POST":
        idRecurso = request.POST.get("idRecurso")
        nombre = request.POST.get("nombre")
        abreviatura = request.POST.get("abreviatura")
        metrica = request.POST.get("metrica")
        tipo = request.POST.get("tipo")
        valorxhora = request.POST.get("valorxhora")
        result = Backend.enviarRecursoMan({"id": idRecurso,
                                        "nombre": nombre,
                                        "abreviatura": abreviatura,
                                        "metrica": metrica,
                                        "tipo": tipo,
                                        "valorXhora": valorxhora})
        
        return render(request, "frontend/crearRecursos.html", result)
        
    return render(request, "frontend/crearRecursos.html", {})

def creacionCategoria(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        carga = request.POST.get("cargaCategoria")
        
        result = Backend.enviarCategoriaMan({"id": id,
                    "nombreCategoria": nombre,
                    "descripcionCategoria": descripcion,
                    "carga_trabajo": carga
                    })
        
        return render(request, "frontend/crearCategoria.html", result)
    
    return render(request, "frontend/crearCategoria.html", {})

def creacionConfiguraciones(request):
    if request.method == "POST":
        idCategoria = request.POST.get("idCategoria")
        idConfiguracion = request.POST.get("idConfiguracion")
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        
        result = Backend.enviarConfiguracionMan({"idCategoria": idCategoria,
                    "idConfiguracion": idConfiguracion,
                    "nombre": nombre,
                    "descripcion": descripcion
                    })
        
        return render(request, "frontend/crearConfiguraciones.html", result)
    return render(request, "frontend/crearConfiguraciones.html", {})