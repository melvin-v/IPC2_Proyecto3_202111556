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
    
    def enviarRecursoMan(data):
        response = requests.post('http://127.0.0.1:4000/crearRecursoMan', json=data)
        return json.loads(response.text)
    
    def enviarCategoriaMan(data):
        response = requests.post('http://127.0.0.1:4000/crearCategoriaMan', json=data)
        return json.loads(response.text)
    
    def enviarConfiguracionMan(data):
        response = requests.post('http://127.0.0.1:4000/crearConfiguracionesMan', json=data)
        return json.loads(response.text)

    def enviarRecursoSubMan(data):
        response = requests.post('http://127.0.0.1:4000/crearRecursosSubMan', json=data)
        return json.loads(response.text)
    
    def enviarClienteMan(data):
        response = requests.post('http://127.0.0.1:4000/crearClienteMan', json=data)
        return json.loads(response.text)
    
    def enviarInstanciaMan(data):
        response = requests.post('http://127.0.0.1:4000/crearInstanciaMan', json=data)
        return json.loads(response.text)
    
    def facturas(data):
        response = requests.post('http://127.0.0.1:4000/facturacion', json=data)
        return json.loads(response.text)
    
    def getFacturas():
        return json.loads(requests.get('http://127.0.0.1:4000/consultarFacturas').text)
    
    def facturaspdf(data):
        response = requests.post('http://127.0.0.1:4000/facturacionpdf', json=data)
        return json.loads(response.text)