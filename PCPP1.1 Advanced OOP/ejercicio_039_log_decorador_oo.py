# Un decorador basado en una clase que deje un registro de log
# en archivo, base de datos o web service en función
# de un parámetro proporcionado por el propio decorador
from enum import Enum

class TipoPersistencia(Enum):
    FICHERO = 1
    BASE_DE_DATOS = 2
    WEB_SERVICE = 3

class GestorPersistenciaFichero:
    def write_log(self, mensaje):
        print('Escribiendo en el fichero', mensaje)

class GestorPersistenciaBBDD:
    def write_log(self, mensaje):
        print('Escribiendo en una base de datos', mensaje)

class GestorPersistenciaWS:
    def write_log(self, mensaje):
        print('Escribiendo en el servicio web', mensaje)

class GestorPersistenciaFactory():
    @staticmethod
    def get_gestor_persistencia(tipo_persistencia : TipoPersistencia):
        match tipo_persistencia:
            case TipoPersistencia.FICHERO:
                return GestorPersistenciaFichero()
            case TipoPersistencia.BASE_DE_DATOS:
                return GestorPersistenciaBBDD()
            case TipoPersistencia.WEB_SERVICE:
                return GestorPersistenciaWS()

class GestorPersistencia:
    def write_log(self, tipo_persistencia : TipoPersistencia, mensaje):
        GestorPersistenciaFactory.get_gestor_persistencia(tipo_persistencia).write_log(mensaje)

# Decorador con función y argumentos
class SuperLogger:
    def __init__(self, tipo_persistencia):
        self.tipo_persistencia = tipo_persistencia

    def __call__(self, funcion_a_decorar):
        def funcion_interna(*args, **kwargs):
            GestorPersistencia().write_log(self.tipo_persistencia, 'foobar')           
            return funcion_a_decorar(*args, **kwargs)
        return funcion_interna

@SuperLogger(tipo_persistencia=TipoPersistencia.WEB_SERVICE)
def sumar(s1, s2):
    return s1+s2

print(sumar(10,12))