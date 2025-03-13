# Crear un decorador que deje registro de log que 
# permita indicar en dónde:
# - Fichero
# - Base de datos
# - Web Service

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

def superlogger(tipo_persistencia : TipoPersistencia):
    def external_wrapper(function_a_decorar):
        def internal_wrapper(*args, **kwargs):
            GestorPersistencia().write_log(tipo_persistencia, 'texto a escribir en el log')           
            return function_a_decorar(*args, **kwargs)
        return internal_wrapper
    return external_wrapper

@superlogger(tipo_persistencia=TipoPersistencia.BASE_DE_DATOS)
def sumar(s1, s2):
    return s1+s2

print(sumar(10,12))