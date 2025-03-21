# función isinstance() --> Determina si un OBJETO es instancia de una clase
# función issubclass() --> Determina si una clase es subclase de otra clase

class Deportista:
    pass

class DeportistaOlimpico(Deportista):
    pass

class SaltadorAltura(DeportistaOlimpico):
    pass

ramon = SaltadorAltura()

print(isinstance(ramon, SaltadorAltura)) # True
print(isinstance(ramon, DeportistaOlimpico)) # True
print(isinstance(ramon, Deportista)) # True

print(issubclass(SaltadorAltura, DeportistaOlimpico)) # True
print(issubclass(SaltadorAltura, Deportista)) # True



