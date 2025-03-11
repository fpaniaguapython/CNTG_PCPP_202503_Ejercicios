class Coche:
    def __init__(self, nombre, precio, consumo, velocidad):
        self.nombre = nombre
        self.precio = precio
        self.consumo = consumo
        self.velocidad = velocidad

    def __lt__(self, other):
        print('lt')
        return self.precio < other.precio
    
    def __gt__(self, other):
        print('gt')
        return self.precio > other.precio
    
    def __eq__(self, other):
        return self.consumo == other.consumo

    def __repr__(self):
        return self.nombre

coche_magan = Coche('Mazda', 20_000, 5.5, 200)
coche_souto = Coche('Toyota', 1_000, 5.5, 180)
coche_paniagua = Coche('Kia', 11_000, 6.5, 175)

coches = [coche_magan, coche_souto, coche_paniagua]
coches_ordenados = sorted(coches, reverse=True)
print(coches_ordenados) # [Mazda, Kia, Toyota]
print(coches) # [Mazda, Toyota, Kia]
coches.sort()
print(coches) # [Toyota, Kia, Mazda]

print(coche_magan == coche_souto) # True
print(coche_magan == coche_paniagua) # False