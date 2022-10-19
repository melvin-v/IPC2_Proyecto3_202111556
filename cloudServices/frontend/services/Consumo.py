from urllib import response
import requests
import json

class Backend:
    def enviarConfiguracion(archivo):
        response = requests.post('http://127.0.0.1:4000/crearConfiguracion',data=archivo)
        return json.loads(response.text)