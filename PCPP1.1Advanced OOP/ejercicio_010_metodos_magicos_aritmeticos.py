class Ordenador:
    def __init__(self, nombre, ghz, ram, disco):
        self.nombre = nombre
        self.ghz = ghz
        self.ram = ram
        self.disco = disco

    # Crear los métodos mágios para sumar ordenadores
    # multiplicar, restar y calcular la longitud de un ordenador

    def __add__(self, other):
        print(self.nombre) # Ordenador1
        return self.ghz + other.ghz
    
    def __mul__(self, other):
        return self.ram * other.ram
    
    def __sub__(self, other):
        return self.disco - other.disco

ordenador1 = Ordenador("Ordenador1", 2.5, 8, 512)
ordenador2 = Ordenador("Ordenador2", 3.5, 16, 1024)

suma = ordenador1 + ordenador2
print(suma) # 6.0

producto = ordenador1 * ordenador2
print(producto) # 128

resta = ordenador1 - ordenador2
print(resta) # -512

