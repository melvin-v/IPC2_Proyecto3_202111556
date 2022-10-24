import xml.etree.ElementTree as ET

class LecturaConsumos:
    def __init__(self, archivo, bdd) -> None:
        self.archivo = archivo
        self.bdd = bdd
        self.consumos = 0
    
    def cargar(self):
        root = ET.fromstring(self.archivo)
        consumos = {"lista_consumos":[]}
        for consumo in root:
            nitCliente = consumo.attrib['nitCliente']
            idInstancia = consumo.attrib['idInstancia']
            for atributo in consumo:
                if atributo.tag == 'tiempo':
                    tiempo = atributo.text
                elif atributo.tag == 'fechaHora':
                    fechaHora = atributo.text
            consumos['lista_consumos'].append({"nitCliente": nitCliente,
                                                     "idInstancia": idInstancia,
                                                     "tiempo": tiempo,
                                                     "fecha_hora": fechaHora})
            self.consumos += 1
            
        return consumos
    
    def mensaje(self):
        return {"consumos":self.consumos, "msg":"correcto"}
            
