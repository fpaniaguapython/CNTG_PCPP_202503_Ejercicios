import abc
import enum

class TipoPersistencia(enum.Enum):
    PICKLE = 1
    FICHERO = 2

class GestorPersistencia(abc.ABC):
    @abc.abstractmethod
    def create(self, id, obj):
        pass

    @abc.abstractmethod
    def read(self, clase, id):
        pass

    # @abc.abstractmethod
    # def update(self, id, obj):
    #     pass

    # @abc.abstractmethod
    # def delete(self, obj):
    #     pass

'''
Implementación de Gestor de Persistencia basado en pickle
'''
import pickle

class GPPickle(GestorPersistencia):
    EXTENSION = '.pickle'

    @classmethod
    def __get_file_name(cls, id):
        return str(id).replace(' ', '_').lower()+cls.EXTENSION

    def create(self, id, obj):
        nombre_fichero = GPPickle.__get_file_name(id)
        with open(nombre_fichero, mode = 'wb') as archivo:
            pickle.dump(obj, archivo)

    def read(self, clase, id):
        nombre_fichero = GPPickle.__get_file_name(id)
        with open(nombre_fichero, mode = 'rb') as archivo:
            objeto = pickle.load(archivo)
        return objeto

'''
Implementación de Gestor de Persistencia basado en ficheros de texto
'''
class GPFichero(GestorPersistencia):
    EXTENSION = '.file'
    DELIMITADOR = '#'

    @classmethod
    def __get_file_name(cls, id):
        return str(id).replace(' ', '_').lower()+cls.EXTENSION

    def create(self, id, obj):
        with open(GPFichero.__get_file_name(id), mode='wt', encoding='utf-8') \
            as archivo:
            for k,v in obj.__dict__.items():
                archivo.write(k+GPFichero.DELIMITADOR+v+'\n')

    def read(self, clase, id):
        with open(GPFichero.__get_file_name(id), mode='rt', encoding='utf-8') \
            as archivo:
            atributos_serializados = archivo.readlines()
            atributos_serializados = [atributo_serializado.replace('\n','') \
                                      for atributo_serializado in atributos_serializados]
            atributos = dict()
            for atributo in atributos_serializados:
                if (len(atributo.strip())!=0): # Si la línea tiene contenido
                    nuevo_atributo = atributo.split(GPFichero.DELIMITADOR)
                    atributos[nuevo_atributo[0]]=nuevo_atributo[1]
            objeto = clase(**atributos) # Desempaquetamos el diccionario
            return objeto

'''
Factory del Gestor de Persistencia
'''
import json

class GestorPersistenciaFactory:
    NOMBRE_FICHERO = 'ejercicio_062_config.json'
    @staticmethod
    def get_gestor_persistencia() -> GestorPersistencia:
        with open(GestorPersistenciaFactory.NOMBRE_FICHERO, 'rt') as archivo:
            configuracion = json.load(archivo)
            if (configuracion['TIPO_PERSISTENCIA']==TipoPersistencia.PICKLE.value):
                return GPPickle()
            if (configuracion['TIPO_PERSISTENCIA']==TipoPersistencia.FICHERO.value):
                return GPFichero()