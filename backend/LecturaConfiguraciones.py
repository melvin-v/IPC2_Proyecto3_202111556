import xml.etree.ElementTree as ET
class LecturaConfiguraciones:
    def __init__(self, archivo, bdd) -> None:
        self.archivo = archivo
        self.bdd = bdd
        self.recursos = 0
        self.categorias = 0
        self.clientes = 0
        self.instancias = 0
        
    def cargar(self):
        #root = ET.parse(self.archivo, parser=ET.XMLParser(encoding='utf-8'))
        root = ET.fromstring(self.archivo)
        configuraciones = self.bdd
        
        for atributo in root:
            if atributo.tag == 'listaRecursos':
                #Recursos
                for recurso in atributo:
                    for caracteristica in recurso:
                        if caracteristica.tag == 'nombre':
                            nombreRecurso = caracteristica.text
                        elif caracteristica.tag == 'abreviatura':
                            abreviaturaRecurso = caracteristica.text
                        elif caracteristica.tag == 'metrica':
                            metricaRecurso = caracteristica.text
                        elif caracteristica.tag == 'tipo':
                            tipoRecurso = caracteristica.text
                        elif caracteristica.tag == 'valorXhora':
                            valorXhoraRecurso = caracteristica.text      
                    configuraciones['lista_recursos'].append({"id": recurso.attrib['id'],
                                                              "nombre": nombreRecurso,
                                                              "abreviatura": abreviaturaRecurso,
                                                              "metrica": metricaRecurso,
                                                              "tipo": tipoRecurso,
                                                              "valorXhora": valorXhoraRecurso})
                    self.recursos += 1
                    
            elif atributo.tag == 'listaCategorias':
                #Categoria
                for categoria in atributo:
                    idCategoria = categoria.attrib['id']
                    for caracteristica in categoria:
                        if caracteristica.tag == 'nombre':
                            nombreCategoria = caracteristica.text
                        elif caracteristica.tag == 'descripcion':
                            descripcionCategoria = caracteristica.text
                        elif caracteristica.tag == 'cargaTrabajo':
                            cargaCategoria = caracteristica.text
                        elif caracteristica.tag == 'listaConfiguraciones':
                            listaConfiguracion = []
                            for listConfiguracion in caracteristica:
                                idListaConf = listConfiguracion.attrib['id']
                                for carLista in listConfiguracion:
                                    if carLista.tag == 'nombre':
                                        nombreConf = carLista.text
                                    elif carLista.tag == 'descripcion':
                                        descripcionConf = carLista.text
                                    elif carLista.tag == 'recursosConfiguracion':
                                        listaRecursos = []
                                        for recursoConf in carLista:
                                            idRecurso = recursoConf.attrib['id']
                                            cantidadRecurso = recursoConf.text
                                            listaRecursos.append({"id":idRecurso,
                                                                  "cantidad":cantidadRecurso})
                                listaConfiguracion.append({"id":idListaConf,
                                                           "nombre": nombreConf,
                                                           "descripcion":descripcionConf,
                                                           "lista_recursos":listaRecursos})
                    
                    configuraciones['lista_categorias'].append({"id": idCategoria,
                                                                "nombre": nombreCategoria,
                                                                "descripcion": descripcionCategoria,
                                                                "carga_trabajo": cargaCategoria,
                                                                "lista_configuraciones": listaConfiguracion})
                    self.categorias += 1 
                    
            elif atributo.tag == 'listaClientes':
                #Clientes
                for cliente in atributo:
                    nitCliente = cliente.attrib['nit']
                    for dato in cliente:
                        if dato.tag == 'nombre':
                            nombreDato = dato.text
                        elif dato.tag == 'usuario':
                            usuarioDato = dato.text
                        elif dato.tag == 'clave':
                            claveDato = dato.text
                        elif dato.tag == 'direccion':
                            direccionDato = dato.text
                        elif dato.tag == 'correoElectronico':
                            correoElectronico = dato.text
                        elif dato.tag == 'listaInstancias':  
                            listaInstancias = []
                            for instancia in dato:
                                instanciaId = instancia.attrib['id']
                                for atributoI in instancia:
                                    if atributoI.tag == 'idConfiguracion':
                                        idConfiguiracion = atributoI.text
                                    elif atributoI.tag == 'nombre':
                                        nombreAtributo = atributoI.text
                                    elif atributoI.tag == 'fechaInicio':
                                        fechaInicioAtributo = atributoI.text
                                    elif atributoI.tag == 'estado':
                                        estadoAtributo = atributoI.text
                                    elif atributoI.tag == 'fechaFinal':
                                        fechaFinalAtributo = atributoI.text
                                
                                listaInstancias.append({"id":instanciaId,
                                                        "idConfiguiracion": idConfiguiracion,
                                                        "nombre": nombreAtributo,
                                                        "fecha_inicio": fechaInicioAtributo,
                                                        "estado": estadoAtributo,
                                                        "fecha_final": fechaFinalAtributo})
                                self.instancias += 1
                                        
                                
                                
                    configuraciones['lista_clientes'].append({"nit":nitCliente,
                                                              "nombre": nombreDato,
                                                              "usuario": usuarioDato,
                                                              "clave": claveDato,
                                                              "direccion": direccionDato,
                                                              "correo_electronico":correoElectronico,
                                                              "lista_instancias": listaInstancias})
                    self.clientes += 1    
                                    
        return configuraciones
    
    def mensaje(self):
        lista = {"recursos":self.recursos, "categorias":self.categorias, "clientes":self.clientes, "instancias":self.instancias}
        return lista
                                        
        