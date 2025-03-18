import abc

class GestorPersistencia(abc.ABC):
    @abc.abstractmethod
    def create(self, id, obj):
        pass

    @abc.abstractmethod
    def read(self, id):
        pass

    # @abc.abstractmethod
    # def update(self, id, obj):
    #     pass

    # @abc.abstractmethod
    # def delete(self, obj):
    #     pass

import pickle

class GestorPersistenciaPickle(GestorPersistencia):
    EXTENSION = '.pickle'

    @classmethod
    def __get_file_name(cls, id):
        return str(id).replace(' ', '_').lower()+cls.EXTENSION

    def create(self, id, obj):
        nombre_fichero = GestorPersistenciaPickle.__get_file_name(id)
        with open(nombre_fichero, mode = 'wb') as archivo:
            pickle.dump(obj, archivo)

    def read(self, id):
        nombre_fichero = GestorPersistenciaPickle.__get_file_name(id)
        with open(nombre_fichero, mode = 'rb') as archivo:
            objeto = pickle.load(archivo)
        return objeto

class GestorPersistenciaFactory:
    @staticmethod
    def get_gestor_persistencia() -> GestorPersistencia:
       return GestorPersistenciaPickle() 