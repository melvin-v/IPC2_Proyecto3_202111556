from flask import Flask, request, jsonify
from flask_cors import CORS
from LecturaConfXML import LecturaConfXML
import json

app = Flask(__name__)
CORS(app)

@app.route("/crearConfiguracion", methods=["POST"])
def crearConfiguracion():
    archivo = open("backend\BDD\configuraciones.json")
    bdd = json.loads(archivo.read())
    archivo.close()
    
    data = request.get_data()
    lector = LecturaConfXML(data, bdd)
    archivoJSON = lector.cargar()
    with open("backend\BDD\configuraciones.json", "w") as outfile: 
        json.dump(archivoJSON, outfile)
    return jsonify(lector.mensaje())

app.run(debug=True, port=4000)

