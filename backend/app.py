from flask import Flask, request, jsonify
from flask_cors import CORS
from LecturaConfiguraciones import LecturaConfiguraciones
from LecturaConsumos import LecturaConsumos
import json

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

app.run(debug=True, port=4000)

