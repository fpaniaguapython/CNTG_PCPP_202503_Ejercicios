# Definición de la clase
class Ordenador(object):

    # Método constructor (inicializador)
    def __init__(self, marca, modelo, precio_unitario):
        self.marca = marca # Declaración de atributo (de instancia) y asignación de valor
        self.modelo = modelo
        self.precio = precio_unitario
        self.calcular_velocidad = 10

    # Método de instancia
    def mostrar_informacion(self):
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
        print('Precio:', self.precio)

class OrdenadorPortatil(Ordenador):
    def __init__(self, marca, modelo, precio_unitario, pulgadas_pantalla):
        super().__init__(marca, modelo, precio_unitario)
        self.pulgadas_pantalla = pulgadas_pantalla


# Creación del objeto o de la instancia
mi_ordenador = Ordenador('Hp', 'Pavilion', 550) # Creacion de una instancia

# Creación del objeto de la clase derivada
mi_ordenador_portatil = OrdenadorPortatil('Hp', 'Pavilion', 550, 15)

# print(mi_ordenador.velocidad_procesador) # AttributeError
# mi_ordenador.calcule_velocidad() # AttributeError

# Función getattr
# Obtención del valor de un atributo
# getattr(mi_ordenador, 'velocidad_procesador') # AttributeError
# Obtención del valor de un atributo con valor de retorno por defecto
velocidad = getattr(mi_ordenador, 'velocidad_procesador', 1000)
print('Velocidad:', velocidad)

# Función setattr
# Establecimiento del valor de un atributo
# print(mi_ordenador.velocidad_procesador) # AttributeError
setattr(mi_ordenador, 'velocidad_procesador', 2000)
print(mi_ordenador.velocidad_procesador) # 2000

# Función hasattr
# Indicar si un objeto tiene o no tiene un atributo
if hasattr(mi_ordenador, 'calcular_velocidad'):
    if (callable(mi_ordenador.calcular_velocidad)):
        mi_ordenador.calcular_velocidad()
    else:
        print('Tengo de eso, pero no es ejecutable')
else:
    print('No tengo de eso')

print(mi_ordenador.__dict__) # Atributos de instancia 
print(Ordenador.__dict__) # Atributos de clase