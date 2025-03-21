# Crear una solución similar a la del ejercicio 22
# con funciones

class Vehiculo:
    def arrancar(self):
        print('Estoy arrancando...')

def circular(self):
    print('Estoy circulando...')

def volar(self):
    print('Estoy volando...')

class Batmovil(Vehiculo):
    def __init__(self):
        Batmovil.circular = circular
        Batmovil.volar = volar

batmovil = Batmovil()
batmovil.arrancar()

batmovil.circular()
batmovil.volar()
    