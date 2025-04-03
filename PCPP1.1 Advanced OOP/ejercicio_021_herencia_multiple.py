class Vehiculo:
    def arrancar(self):
        print('Estoy arrancando...')

class Automovil(Vehiculo):
   def circular(self):
        print('Estoy circulando...')

class Avion(Vehiculo):
    def volar(self):
        print('Estoy volando...')

class Batmovil(Automovil, Avion): # Es una herencia múltiple
    pass

batmovil = Batmovil()
batmovil.arrancar()
batmovil.circular()
batmovil.volar()