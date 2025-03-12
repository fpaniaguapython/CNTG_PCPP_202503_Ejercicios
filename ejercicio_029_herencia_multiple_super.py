class Vehiculo:
    def __init__(self, nombre):
        print('__init__ de Vehiculo')
        self.nombre = nombre
    def arrancar(self):
        print('Estoy arrancando...')

class Automovil(Vehiculo):
    def __init__(self, nombre, velocidad):
        print('__init__ de Automovil')
        Vehiculo.__init__(self, nombre)
        self.velocidad = velocidad

    def atacar(self):
        print(f'Soy {self.nombre} y estoy atacando como automóvil...')

class Avion(Vehiculo):
    def __init__(self, nombre, altitud):
        print('__init__ de Avion')
        Vehiculo.__init__(self, nombre)
        self.altitud = altitud

    def atacar(self):
        print(f'Soy {self.nombre} y estoy atacando como avión...')

class Batmovil(Automovil, Avion): # Es una herencia múltiple
    def __init__(self, nombre, velocidad, altitud):
        Automovil.__init__(self, nombre, velocidad)
        Avion.__init__(self, nombre, altitud)

    def atacar(self):
        Automovil.atacar(self)
        Avion.atacar(self)

batmovil = Batmovil('Batmovil', 300, 5_000)
batmovil.atacar()