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

    def circular(self):
        self.vehiculo_terrestre.circular()

    def volar(self):
        self.vehiculo_aereo.volar()

batmovil = Batmovil()
batmovil.arrancar()

batmovil.circular()
batmovil.volar()