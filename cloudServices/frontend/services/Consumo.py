from urllib import response
import requests
import json

class Backend:
    def enviarConfiguracion(archivo):
        fileDic = {"file": archivo}
        response = requests.post('http://127.0.0.1:4000/crearConfiguracion',data=fileDic)
        return json.loads(response.text)
    