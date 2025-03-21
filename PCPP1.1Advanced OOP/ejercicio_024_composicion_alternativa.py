class Vehiculo:
    def arrancar(self):
        print('Estoy arrancando...')

class VehiculoTerrestre():
   def circular(self):
        print('Estoy circulando...')

class VehiculoAereo():
    def volar(self):
        print('Estoy volando...')

class Batmovil(Vehiculo):
    def __init__(self):
        Batmovil.circular = VehiculoTerrestre.circular
        Batmovil.volar = VehiculoAereo.volar

batmovil = Batmovil()
batmovil.arrancar()

batmovil.circular()
batmovil.volar()