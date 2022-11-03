from flask import Flask, request, jsonify
from flask_cors import CORS
from LecturaConfiguraciones import LecturaConfiguraciones
from LecturaConsumos import LecturaConsumos
import json, re, datetime, random, jinja2, pdfkit

app = Flask(__name__)
CORS(app)

@app.route("/crearConfiguracion", methods=["POST"])
def crearConfiguracion():
    archivo = open("backend\BDD\configuraciones.json")
    bdd = json.loads(archivo.read())
    archivo.close()
    try:
        data = str(request.get_data())
        cSplit = data.split('<?xml version="1.0"?>')
        splitN = cSplit[1].split('\\r\\n')
        cadenaFinal = '' 
        for numberPalabra in range(len(splitN)):
            if numberPalabra <= (len(splitN) - 3):
                cadenaFinal += splitN[numberPalabra]
        cadena = '<?xml version="1.0"?>' + cadenaFinal
        lector = LecturaConfiguraciones(cadena, bdd)
        archivoJSON = lector.cargar()
        with open("backend\BDD\configuraciones.json", "w") as outfile: 
            json.dump(archivoJSON, outfile)
        return jsonify(lector.mensaje())
    except:
        data = request.get_data()
        lector = LecturaConfiguraciones(data, bdd)
        archivoJSON = lector.cargar()
        with open("backend\BDD\configuraciones.json", "w") as outfile: 
            json.dump(archivoJSON, outfile)
        return jsonify(lector.mensaje())

@app.route("/crearConsumo", methods=["POST"])
def crearConsumo():
    archivo = open("backend\BDD\consumos.json")
    bdd = json.loads(archivo.read())
    archivo.close()
    try:      
        data = str(request.get_data())
        cSplit = data.split('<?xml version="1.0"?>')
        splitN = cSplit[1].split('\\r\\n')
        cadenaFinal = '' 
        for numberPalabra in range(len(splitN)):
            if numberPalabra <= (len(splitN) - 3):
                cadenaFinal += splitN[numberPalabra]
        cadena = '<?xml version="1.0"?>' + cadenaFinal
        lector = LecturaConsumos(cadena, bdd)
        archivoJSON = lector.cargar()
        with open("backend\BDD\consumos.json", "w") as outfile: 
            json.dump(archivoJSON, outfile)
        return jsonify(lector.mensaje())
    except:
        data = request.get_data()
        lector = LecturaConsumos(data, bdd)
        archivoJSON = lector.cargar()
        with open("backend\BDD\consumos.json", "w") as outfile: 
            json.dump(archivoJSON, outfile)
        return jsonify(lector.mensaje())

@app.route("/consultarDatos", methods=["GET"])
def consultarDatos():
        archivoConfiguracion = open("backend\BDD\configuraciones.json")
        archivoConsumos = open("backend\BDD\consumos.json")
        bddJsonConf = json.loads(archivoConfiguracion.read())
        bddJsonCons = json.loads(archivoConsumos.read())
        archivoConfiguracion.close()
        archivoConsumos.close()
        archivoRetorno = {"configuraciones":bddJsonConf,
                          "consumos":bddJsonCons}
        return jsonify(archivoRetorno)
    
@app.route("/crearRecursoMan", methods=["POST"])
def crearRecursoMan():
    archivo = open("backend\BDD\configuraciones.json")
    bdd = json.loads(archivo.read())
    archivo.close()
    listaID = []
    for recurso in bdd["lista_recursos"]:
        listaID.append(recurso["id"])
        
    errores = []
    body = request.get_json()
    idRecurso = body["id"]
    nombre = body["nombre"]
    abreviatura = body["abreviatura"]
    metrica = body["metrica"]
    tipo = body["tipo"]
    valorxhora = body["valorXhora"]
    
    if idRecurso in listaID:
        errores.append("ID ya usado")
    if tipo in ["Hardware", "Software"]:
        pass
    else:
        errores.append("El tipo es erroneo")
    
    if len(errores) == 0:
        bdd['lista_recursos'].append({"id": idRecurso,
                                        "nombre": nombre,
                                        "abreviatura": abreviatura,
                                        "metrica": metrica,
                                        "tipo": tipo,
                                        "valorXhora": valorxhora})
        
        with open("backend\BDD\configuraciones.json", "w") as outfile: 
            json.dump(bdd, outfile)
            
        return jsonify({"msg":"correcto"})
    
    else:
        return jsonify({"msg":"incorrecto", "errores":errores})
    
@app.route("/crearCategoriaMan", methods=["POST"])
def crearCategoriaMan():
    archivo = open("backend\BDD\configuraciones.json")
    bdd = json.loads(archivo.read())
    archivo.close()
    listaID = []
    for recurso in bdd["lista_categorias"]:
        listaID.append(recurso["id"])
      
    errores = []
    body = request.get_json()
    
    configuracion = {"id": body["id"],
                    "nombre": body["nombreCategoria"],
                    "descripcion": body["descripcionCategoria"],
                    "carga_trabajo": body["carga_trabajo"],
                    "lista_configuraciones": []} 
    
    if body["id"] in listaID:
        errores.append("ID ya usado")
        
    if len(errores) == 0:
        bdd["lista_categorias"].append(configuracion)
        with open("backend\BDD\configuraciones.json", "w") as outfile: 
            json.dump(bdd, outfile)
            
        return jsonify({"msg":"correcto"})
    
    else:
        return jsonify({"msg":"incorrecto", "errores":errores})
    
@app.route("/crearConfiguracionesMan", methods=["POST"])
def crearConfiguracionesMan():
    archivo = open("backend\BDD\configuraciones.json")
    bdd = json.loads(archivo.read())
    archivo.close()
    listaIDCategoria = []
    listaIDConfiguracion = []
    counter = 0
    counterConfiguracion = 0
            
    errores = []
    body = request.get_json()
    
    for categoria in bdd["lista_categorias"]:
        listaIDCategoria.append(categoria["id"])
        for configuracion in categoria["lista_configuraciones"]:
            if categoria["id"]==body["idCategoria"]:
                listaIDConfiguracion.append(configuracion["id"])
        if categoria["id"]==body["idCategoria"]:
            counterConfiguracion = counter
        counter += 1
    if body["idCategoria"] in listaIDCategoria:
        pass
    else:
        errores.append("ID categoria no existe")
    if body["idConfiguracion"] in listaIDConfiguracion:
        errores.append("ID configuracion ya usado")
        
    idConfiguracion = body["idConfiguracion"]
    nombre = body["nombre"]
    descripcion = body["descripcion"]
    
    if len(errores) == 0:
        bdd["lista_categorias"][counterConfiguracion]['lista_configuraciones'].append({"id":idConfiguracion,
                                                     "nombre": nombre,
                                                     "descripcion":descripcion})
        with open("backend\BDD\configuraciones.json", "w") as outfile: 
            json.dump(bdd, outfile)
            
        return jsonify({"msg":"correcto"})
    
    else:
        return jsonify({"msg":"incorrecto", "errores":errores})
    
@app.route("/crearRecursosSubMan", methods=["POST"])
def crearRecursosMan():
    archivo = open("backend\BDD\configuraciones.json")
    bdd = json.loads(archivo.read())
    archivo.close()
    listaIDCategoria = []
    listaIDConfiguracion = []
    listaIDRecurso = []
    counter1 = 0
    counter2 = 0
    counterConfiguracion = 0
    counterCategoria = 0
    errores = []
    body = request.get_json()
    
    for categoria in bdd["lista_categorias"]:
        listaIDCategoria.append(categoria["id"])
        for configuracion in categoria["lista_configuraciones"]:
            if categoria["id"]==body["idCategoria"]:
                listaIDConfiguracion.append(configuracion["id"])
        if categoria["id"]==body["idCategoria"]:
            counterCategoria = counter1
            try:
                for recurso in configuracion["lista_recursos"]:
                    if recurso["id"]==body["idRecurso"]:
                        listaIDConfiguracion.append(configuracion["id"])
                        
                if recurso["id"]==body["idRecurso"]:
                    counterConfiguracion = counter2
            except:
                pass
            
            counter2 += 1        
        counter1 += 1
    if body["idCategoria"] in listaIDCategoria:
        pass
    else:
        errores.append("ID categoria no existe")
    if body["idConfiguracion"] in listaIDConfiguracion:
        pass
    else:
        errores.append("ID configuracion no existe")
    if body["idRecurso"] in listaIDRecurso:
        errores.append("ID recurso ya usado")
            
    idRecurso = body["idRecurso"]
    cantidad = body["cantidad"]
        
    if len(errores) == 0:
        bdd["lista_categorias"][counterCategoria]['lista_configuraciones'][counterConfiguracion]['lista_recursos'].append({"id":idRecurso,
                                                        "cantidad":cantidad})
        with open("backend\BDD\configuraciones.json", "w") as outfile: 
            json.dump(bdd, outfile)
            
        return jsonify({"msg":"correcto"})
    
    else:
        return jsonify({"msg":"incorrecto", "errores":errores})

@app.route("/crearClienteMan", methods=["POST"])
def crearClienteMan():
    archivo = open("backend\BDD\configuraciones.json")
    bdd = json.loads(archivo.read())
    archivo.close()
    listaNit = []
    for recurso in bdd["lista_clientes"]:
        listaNit.append(recurso["nit"])
      
    errores = []
    body = request.get_json()
    
    cliente = {"nit": body["nit"],
                    "nombre": body["nombre"],
                    "usuario": body["usuario"],
                    "clave": body["clave"],
                    "direccion": body["direccion"],
                    "correo_electronico": body["correo_electronico"],
                    "lista_instancias":[]} 
    
    if body["nit"] in listaNit:
        errores.append("Nit ya usado")
        
    if len(errores) == 0:
        bdd["lista_clientes"].append(cliente)
        with open("backend\BDD\configuraciones.json", "w") as outfile: 
            json.dump(bdd, outfile)
            
        return jsonify({"msg":"correcto"})
    
    else:
        return jsonify({"msg":"incorrecto", "errores":errores})
    
@app.route("/crearInstanciaMan", methods=["POST"])
def crearInstanciaMan():
    archivo = open("backend\BDD\configuraciones.json")
    bdd = json.loads(archivo.read())
    archivo.close()
    listaNit = []
    listaID = []
    counter = 0
    counterCliente = 0
            
    errores = []
    body = request.get_json()
    
    for cliente in bdd["lista_clientes"]:
        listaNit.append(cliente["nit"])
        for instancia in cliente["lista_instancias"]:
            if cliente["nit"]==body["id"]:
                listaID.append(instancia["id"])
        if cliente["nit"]==body["nit"]:
            counterCliente = counter
        counter += 1
    if body["nit"] in listaNit:
        pass
    else:
        errores.append("Nit no existe")
    if body["idConfiguracion"] in listaNit:
        errores.append("ID instancia ya usado")
        
    str_patron = r'([0-2][0-9]|3[0-1])(/)(0[1-9]|1[0-2])\2(\d{4})'
    patron = re.compile(str_patron)
    fechaInicio = patron.search(body["fecha_inicio"])
    fechaFinal = patron.search(body["fecha_final"])
    
    if fechaInicio is None:
        errores.append("Formato de fecha inicial incorrecto")
        
    if fechaFinal is None:
        errores.append("Formato de fecha final incorrecto")
        
    id = body["nit"]
    idConfiguracion = body["idConfiguracion"]
    nombre = body["nombre"]
    fecha_inicio = body["fecha_inicio"]
    estado = body["estado"]
    fecha_final = body["fecha_final"]
    
    if len(errores) == 0:
        bdd["lista_clientes"][counterCliente]["lista_instancias"].append({"id":id,
                                                                          "idConfiguracion":idConfiguracion,
                                                                          "nombre":nombre,
                                                                          "fecha_inicio":fecha_inicio,
                                                                          "estado":estado,
                                                                          "fecha_final":fecha_final})
        with open("backend\BDD\configuraciones.json", "w") as outfile: 
            json.dump(bdd, outfile)
            
        return jsonify({"msg":"correcto"})
    
    else:
        return jsonify({"msg":"incorrecto", "errores":errores})
   
@app.route("/facturacion", methods=["POST"])
def facturacion():
    archivo = open("backend\BDD\consumos.json")
    bdd = json.loads(archivo.read())
    archivo.close()
    
    archivoFactura = open("backend\BDD\dfacturas.json")
    facturas = json.loads(archivoFactura.read())
    archivoFactura.close()
    contadorVueltas = 0
    countfacturas = 0
    body = request.get_json()
    fI = body["startDate"].split("/")
    fechaInicial = datetime.date(int(fI[2]), int(fI[1]), int(fI[0]), )
    fE = body["endDate"].split("/")
    fechaFinal = datetime.date(int(fE[2]), int(fE[1]), int(fE[0]))
    for consumo in bdd["lista_consumos"]:
        str_patron = r'([0-2][0-9]|3[0-1])(/)(0[1-9]|1[0-2])\2(\d{4})'
        patron = re.compile(str_patron)
        primero = consumo["fecha_hora"]
        segundo = patron.search(primero)
        tercero = segundo.group(0)
        fEvaluar = tercero.split("/")
        fechaEvaluar = datetime.date(int(fEvaluar[2]), int(fEvaluar[1]), int(fEvaluar[0]))
        if (fechaInicial >= fechaEvaluar <= fechaFinal) and consumo["facturado"] == "0":
            numero = random.randint(1,10000)
            facturas["facturas"].append({"NumeroFactura":numero,
                                     "nitCliente": consumo["nitCliente"],
                                     "idInstancia": consumo["idInstancia"],
                                     "tiempo": consumo["tiempo"],
                                     "fecha": body["endDate"]})
            countfacturas += 1
            bdd["lista_consumos"][contadorVueltas]["facturado"] = "1"
        contadorVueltas += 1
    mensaje = "Se añadieron " + str(countfacturas)     
    with open("backend\BDD\consumos.json", "w") as outfile: 
            json.dump(bdd, outfile)
    with open("backend\BDD\dfacturas.json", "w") as outfile: 
            json.dump(facturas, outfile)
            
            
    return jsonify({"msg":mensaje}) 

@app.route("/consultarFacturas", methods=["GET"])
def consultarFacturas():
        archivo = open("backend\BDD\dFacturas.json")
        bddJsonfac = json.loads(archivo.read())
        archivo.close()
        archivoRetorno = {"facturas":bddJsonfac}
        return jsonify(archivoRetorno)  
    
@app.route("/facturacionpdf", methods=["POST"])
def facturacionpdf():
    archivo = open("backend\BDD\dFacturas.json")
    bddJsonfac = json.loads(archivo.read())
    archivo.close()
    body = request.get_json()
    facturaF = {}
    for factura in bddJsonfac["facturas"]:
        if str(factura["NumeroFactura"])==str(body["idFactura"]):
            facturaF = factura
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("backend\\"))
    template = env.get_template("lateFactura.html")
    html = template.render(facturaF)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_string(html, "C:\\Users\\melvi\\Desktop\\Factura.pdf" , configuration=config)
    
    return jsonify({"ruta":"C:\\Users\\melvi\\Desktop\\Factura.pdf"})
            
app.run(debug=True, port=4000)

