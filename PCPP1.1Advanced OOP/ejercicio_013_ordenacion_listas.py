class Coche:
    def __init__(self, nombre, precio, consumo, velocidad):
        self.nombre = nombre
        self.precio = precio
        self.consumo = consumo
        self.velocidad = velocidad
    
    def __repr__(self):
        return self.nombre

coche_magan = Coche('Mazda', 20_000, 5.5, 200)
coche_souto = Coche('Toyota', 1_000, 5.5, 180)
coche_paniagua = Coche('Kia', 11_000, 6.5, 175)

coches = [coche_magan, coche_souto, coche_paniagua]
# Versión 'tradicional'
def valorar_coche(coche):
    return len(coche.nombre)

coches.sort(key=valorar_coche)
print(coches) # [Kia, Mazda, Toyota]

# Versión con lambda
coches.sort(key=lambda coche: coche.consumo)
print(coches) # [Mazda, Toyota, Kia]
