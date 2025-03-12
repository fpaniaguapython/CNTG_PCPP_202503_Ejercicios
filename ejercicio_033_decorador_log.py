# Crear un decorador que deje un log con el timestamp de la ejecución de la función 
# y el nombre de la función que se está ejecutando.
from datetime import datetime

LOG_FILE_NAME = 'log.csv'

def escribir_log(*textos:str):
    with open(LOG_FILE_NAME, mode='at') as fichero:
        for texto in textos[:-1]:
            fichero.write(texto + ',')
        fichero.write(textos[-1])
        fichero.write('\n')

def logger(funcion):
    def inner_function(*args, **kwargs):
        ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        nombre_funcion = funcion.__name__
        escribir_log(ahora, nombre_funcion)
        retorno = funcion(*args, **kwargs)
        return retorno
    return inner_function

@logger
def saludar():
    print('Hola')

@logger()
def despedir():
    print('Agur')

@logger
def sumar(a, b):
    return a+b

saludar()
despedir()
print(sumar(4,8))