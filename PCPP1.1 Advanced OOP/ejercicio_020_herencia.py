class Artefacto:
    pass

class Vehiculo(Artefacto):
    pass

class Automovil(Vehiculo):
    pass

mi_automovil = Automovil() # Es instancia de Automovil, de Vehiculo y de Artefacto

class Avion(Vehiculo):
    pass

class Batmovil(Automovil, Avion): # Es una herencia múltiple
    pass