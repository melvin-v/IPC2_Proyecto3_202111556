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

def creacionRescursoSub(request):
    if request.method == "POST":
        idCategoria = request.POST.get("idCategoria")
        idConfiguracion = request.POST.get("idConfiguracion")
        idRecurso = request.POST.get("idRecurso")
        cantidad = request.POST.get("cantidad")
        
        result = Backend.enviarRecursoSubMan({"idCategoria": idCategoria,
                    "idConfiguracion": idConfiguracion,
                    "idRecurso": idRecurso,
                    "cantidad": cantidad
                    })
        
        return render(request, "frontend/crearRecursoSub.html", result)
    
    return render(request, "frontend/crearRecursoSub.html", {})

def creacionCliente(request):
    if request.method == "POST":
        nit = request.POST.get("nit")
        nombre = request.POST.get("nombre")
        usuario = request.POST.get("usuario")
        clave = request.POST.get("clave")
        direccion = request.POST.get("direccion")
        correo = request.POST.get("correo_electronico")
        
        result = Backend.enviarClienteMan({"nit": nit,
                    "nombre": nombre,
                    "usuario": usuario,
                    "clave":clave,
                    "direccion":direccion,
                    "correo_electronico":correo
                    })
        
        return render(request, "frontend/crearCliente.html", result)
    
    return render(request, "frontend/crearCliente.html", {})

def creacionInstancia(request):
    if request.method == "POST":
        nit = request.POST.get("nit")
        id = request.POST.get("id")
        idConfiguracion = request.POST.get("idConfiguracion")
        nombre = request.POST.get("nombre")
        fecha_inicio = request.POST.get("fecha_inicio")
        estado = request.POST.get("estado")
        fecha_final = request.POST.get("fecha_final")
        
        result = Backend.enviarInstanciaMan({"nit": nit,
                    "id": id,
                    "idConfiguracion":idConfiguracion,
                    "nombre": nombre,
                    "fecha_inicio":fecha_inicio,
                    "estado":estado,
                    "fecha_final":fecha_final
                    })
        
        return render(request, "frontend/crearInstancia.html", result)
    
    return render(request, "frontend/crearInstancia.html", {})