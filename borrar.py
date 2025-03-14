def fsaludar(self):
    print(f'Hola {self.nombre}')


class Humano:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def get_nombre(self):
        return self.nombre


sonia = Humano('Sonia')
sonia.salario = 50_000 # Agregamos atributo a instancia
Humano.saludar = fsaludar
sonia.saludar()

print(sonia.__dict__)

jose_luis = Humano('José Luis')
print(jose_luis.__dict__)

Humano.edad_maxima = 100
print(Humano.edad_maxima)