def f_metodo_instancia(self):
    print('Ejecutando método de instancia...:', self.numero)

@classmethod
def f_metodo_clase(cls):
    print('Ejecutando método de clase...:', cls.atributo_de_clase)

@staticmethod
def f_metodo_estatico():
    print('Ejecutando método estático...')

def decorador(clase_a_decorar):
    clase_a_decorar.metodo_instancia = f_metodo_instancia
    clase_a_decorar.metodo_clase = f_metodo_clase
    clase_a_decorar.metodo_estatico = f_metodo_estatico
    clase_a_decorar.atributo_de_clase = 'Soy un atributo de clase'
    
    # A partir de aquí se está asociando atributos de instancia modificando el __init__ original
    original_init = clase_a_decorar.__init__
    def inner_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.atributo_instancia = 'Soy un atributo de instancia'
    clase_a_decorar.__init__ = inner_init

    return clase_a_decorar

@decorador
class Factura:
    def __init__(self, numero):
        self.numero = numero

    def get_numero(self):
        return self.numero
    
factura_1 = Factura(101)
factura_2 = Factura(102)

factura_1.metodo_instancia() # Ejecutando método de instancia...: 101
factura_1.metodo_clase() # Ejecutando método de clase...: Soy un atributo de clase
factura_1.metodo_estatico()# Ejecutando método estático...

factura_2.metodo_instancia() # Ejecutando método de instancia...: 102
factura_2.metodo_clase() # Ejecutando método de clase...: Soy un atributo de clase
factura_2.metodo_estatico() # Ejecutando método estático...

print(factura_1.atributo_instancia) # Soy un atributo de instancia
print(factura_2.atributo_instancia) # Soy un atributo de instancia
factura_1.atributo_instancia = 'Soy un atributo de instancia modificado'
print(factura_1.atributo_instancia) # Soy un atributo de instancia modificado
print(factura_2.atributo_instancia) # Soy un atributo de instancia

Factura.atributo_de_clase = 'Soy un atributo de clase modificado'
factura_1.metodo_clase() # Ejecutando método de clase...: Soy un atributo de clase modificado
factura_2.metodo_clase() # Ejecutando método de clase...: Soy un atributo de clase modificado

print(Factura.__dict__) # metodo_instancia, metodo_clase, metodo_estatico, atributo_de_clase
print(factura_1.__dict__) # numero, atributo_instancia