class Ordenador:
    def __init__(self, nombre, ghz, ram, disco):
        self.nombre = nombre
        self.ghz = ghz
        self.ram = ram
        self.disco = disco

    def __add__(self, other):
        suma = Ordenador(self.nombre+other.nombre, self.ghz+other.ghz, self.ram+other.ram, self.disco+other.disco)
        return suma
    
    def __str__(self):
        return f'{self.nombre} {self.ghz} {self.ram} {self.disco}'

ordenador1 = Ordenador("Ordenador1", 2.5, 8, 512)
ordenador2 = Ordenador("Ordenador2", 3.5, 16, 1024)
ordenador3 = Ordenador("Ordenador3", 1.5, 32, 128)

suma = ordenador1 + ordenador2
print(suma) # Ordenador1Ordenador2 6.0 24 1536

suma = ordenador1 + ordenador2 + ordenador3
print(suma) # Ordenador1Ordenador2Ordenador3 7.5 56 1664
