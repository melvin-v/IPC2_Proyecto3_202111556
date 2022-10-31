import xml.etree.ElementTree as ET
import re

class LecturaConsumos:
    def __init__(self, archivo, bdd) -> None:
        self.archivo = archivo
        self.bdd = bdd
        self.consumos = 0
        self.errores = []
    
    def cargar(self):
        root = ET.fromstring(self.archivo)
        consumos = {"lista_consumos":[]}
        for consumo in root:
            nitCliente = consumo.attrib['nitCliente']
            idInstancia = consumo.attrib['idInstancia']
            for atributo in consumo:
                if atributo.tag == 'tiempo':
                    patronT = re.compile(r'[0-9]+([.])?([0-9]+)?')
                    listaT = patronT.search(atributo.text)
                    try:
                        tiempo = listaT.group(0)
                    except:
                        tiempo = atributo.text
                elif atributo.tag == 'fechaHora':
                    fechaHora = atributo.text
            str_patron = r'([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})(\s)([0-1][0-9]|2[0-3])(:)([0-5][0-9])'
            patron = re.compile(str_patron)
            horaCorrecta = patron.search(fechaHora)
            if horaCorrecta is not None:
                consumos['lista_consumos'].append({"nitCliente": nitCliente,
                                                        "idInstancia": idInstancia,
                                                        "tiempo": tiempo,
                                                        "fecha_hora": horaCorrecta.group(0),
                                                        "facturado":"0"})
                self.consumos += 1
            else:
                mensaje = "El formato de la hora y fecha es incorrecto de " + fechaHora
                self.errores.append({"HoraFecha":mensaje})
            
        return consumos
    
    def mensaje(self):
        return {"consumos":self.consumos, "msg":"correcto", "errores":self.errores}
            
