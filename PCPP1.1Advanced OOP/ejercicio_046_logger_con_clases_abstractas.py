'''
Crear un sistema de log basado en clases abstractas.
La clase abstracta dispondrá de un método 'concreto' que generará
el texto a dejar en el log.

Las implementaciones del sistema de log serán: fichero, bbdd y ws

La decisión de elegir uno u otro sistema se hará a partir de la lectura
de un fichero de configuración.
'''
import json
import enum
from abc import ABC, abstractmethod

class TipoLog(enum.Enum):
    FICHERO=0
    BBDD=1
    WS=2

def get_tipo():
    fichero_config = open('config_logger.json','rt')
    configuracion = json.load(fichero_config)
    tipo = configuracion['tipo']
    fichero_config.close()
    return tipo

class Logger(ABC):
    def generar_log(self, mensaje : str) -> str:
        return mensaje + ' 14:03:2025 19:10'
    
    @staticmethod
    def get_logger():
        tipo_log = get_tipo()
        match tipo_log:
            case TipoLog.FICHERO.value:
                return LoggerFichero()
            case TipoLog.BBDD.value:
                return LoggerBBDD()
            case TipoLog.WS.value:
                return LoggerWS()
            case _:
                raise Exception('No hay disponible ningún servicio de LOG')
    
    @abstractmethod
    def escribir_log(self, mensaje):
        pass

class LoggerFichero(Logger):
    def escribir_log(self, mensaje):
        log = self.generar_log('Fichero. ' + mensaje)
        print(log)

class LoggerBBDD(Logger):
    def escribir_log(self, mensaje):
        log = self.generar_log('BBDD. ' + mensaje)
        print(log)

class LoggerWS(Logger):
    def escribir_log(self, mensaje):
        log = self.generar_log('WS.' + mensaje)
        print(log)

servicio_log = Logger.get_logger()
if (isinstance(servicio_log, Logger)):
    servicio_log.escribir_log('Receta de la tortilla con patatas (con cebolla)') 
else:
    raise TypeError('Se ha obtenido algo que no es un Logger')