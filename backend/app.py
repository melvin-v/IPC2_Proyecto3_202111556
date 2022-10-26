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
        

app.run(debug=True, port=4000)

