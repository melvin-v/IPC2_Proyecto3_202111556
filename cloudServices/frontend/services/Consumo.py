import requests
import json

class Backend:
    def enviarConfiguracion(archivo):
        fileDic = {"file": archivo}
        response = requests.post('http://127.0.0.1:4000/crearConfiguracion',files=fileDic)
        return json.loads(response.text)
    
    def enviarConsumo(archivo):
        fileDic = {"file": archivo}
        response = requests.post('http://127.0.0.1:4000/crearConsumo',files=fileDic)
        return json.loads(response.text)
    
    def getDatos():
        return json.loads(requests.get('http://127.0.0.1:4000/consultarDatos').text)
        
    