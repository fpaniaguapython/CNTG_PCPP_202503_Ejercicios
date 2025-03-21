class Videojuego(object):
    def __init__(self, titulo, plataforma):
        self.titulo = titulo
        self.plataforma = plataforma
    def __eq__(self, value):
        return self.titulo == value.titulo

# operador ==, utiliza __eq__
# operador is, utiliza la identidad
# función id proporciona el identificador

v1 = Videojuego('Call Of Duty', 'PS4')
v2 = Videojuego('Call Of Duty', 'PC')

print(v1==v2) # True, después de programar __eq__
print(v1 is v2) # False (no depende de __eq__)
print(id(v1)) # 2108873009408
print(id(v2)) # 2108875884816

# Asignación de referencia
v2 = v1
print(v1==v2) # True, sin necesidad el __eq__
print(id(v1)) # 2108873009408
print(id(v2)) # 2108873009408