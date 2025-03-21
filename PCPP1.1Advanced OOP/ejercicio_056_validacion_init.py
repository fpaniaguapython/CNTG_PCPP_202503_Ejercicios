'''
Crear una clase excepcion propia que sea capaz de escribir en un fichero el 
log del error que ha ocurrido.

Clase Pedido. En el __init__ tiene los siguientes argumentos:
- Número de productos
- Precio unitario

Verificar en el __init__ que el número de productos es un número entero > 0
Verificar en el __init__ que el precio unitario es un número entero > 0
'''
from datetime import datetime

class DatosPedidoError(Exception):
    LOG_FILE_NAME = 'e56_log.txt'
    def __init__(self, *args):
        if len(args)>0:
            self.message = args[0]
            super().__init__(*args)
        else:
            self.message = 'Ha ocurrido un error desconocido'
            super().__init__(self.message)

    def write_log(self):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        with open(DatosPedidoError.LOG_FILE_NAME, mode='at', encoding='utf-8') as fichero:
            fichero.write(timestamp)
            fichero.write(',')
            fichero.write(self.message)
            fichero.write('\n')

class Pedido:
    @staticmethod
    def __validar_campos(numero_productos, precio_unitario):
        if (not isinstance(numero_productos, int) or not isinstance(precio_unitario, int)):
            raise DatosPedidoError('Alguno de los argumentos del pedido no es un número entero')
        if (numero_productos<=0 or precio_unitario<=0):
            raise DatosPedidoError('Alguno de los argumentos del pedido no tiene un valor positivo')
        
    def __init__(self, numero_productos, precio_unitario):
        try:
            Pedido.__validar_campos(numero_productos, precio_unitario)
        except DatosPedidoError as dpe:
            dpe.write_log()
            raise dpe
        self.numero_productos = numero_productos
        self.precio_unitario = precio_unitario

try:
    pedido = Pedido(10, 20)
except DatosPedidoError as dpe:
    print('DatosPedidoError:', dpe)
except Exception as ex:
    print('Exception:', ex)
else:
    print('¡Pedido realizado!')