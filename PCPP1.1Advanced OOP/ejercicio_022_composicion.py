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
        self.vehiculo_terrestre = VehiculoTerrestre()
        self.vehiculo_aereo = VehiculoAereo()

batmovil = Batmovil()
batmovil.arrancar()

batmovil.vehiculo_terrestre.circular()
batmovil.vehiculo_aereo.volar()