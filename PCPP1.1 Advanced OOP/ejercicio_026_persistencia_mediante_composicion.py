import json

class FactoryPersistencia:
    @staticmethod
    def get_persistence_manager():
        return GestorPersistenciaFichero()

class GestorPersistenciaFichero:
    def save(self, nombre_fichero, objeto):
        fichero = open(nombre_fichero, mode='wt', encoding='utf-8')
        json.dump(objeto.to_dict(), fichero)
        fichero.close()

class Factura:
    def __init__(self, numero, importe):
        self.numero = numero
        self.importe = importe
        self.__gestor_persistencia = FactoryPersistencia.get_persistence_manager()

    # Necesario porque la función dump del json solo admite diccionarios
    def to_dict(self): # Convierte los datos del objeto Factura a diccionario
        return {
            'numero': self.numero,
            'importe': self.importe
        }
 
    def save(self):
        self.__gestor_persistencia.save(str(self.numero) + '.txt', self)
    
f = Factura(104, 10_000)
f.save()
