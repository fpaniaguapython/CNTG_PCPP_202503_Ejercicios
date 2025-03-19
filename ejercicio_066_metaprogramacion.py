# Metaclase

# Función type --> Todas las clases son instancias de type
a = 3
print(type(a)) # <class 'int'>
print(type(int)) # <class 'type'>

class Autor:
    pass
autor = Autor()
print(type(autor)) # <class '__main__.Autor'>
print(type(Autor)) # <class 'type'>

# ********************
# Atributos especiales
# ********************

print(Autor.__name__) # Autor (Nombre de la clase)
# print(autor.__name__) # AttributeError

print(Autor.__class__) # <class 'type'>
print(autor.__class__) # <class '__main__.Autor'>

print(Autor.__bases__) # (<class 'object'>,) -> Las clases de las que hereda directamente
# print(autor.__bases__) # AttributeError

print(Autor.__dict__) # Atributos de clase y todos los métodos
print(autor.__dict__) # Atributos de instancia

# Función type que permite crear clases
# Con un argumento, nos dice de qué tipo es lo que le pasamos (ver más arriba)
# Con tres argumentos, construye una clase
# x -> Nombre de la clase (va al atributo __name__)
# y -> Tupla con las clases de las que hereda la nueva clase (va a ir al atributo __bases__)
# z -> Diccionario que métodos y atributos de la clase (va a ir al __dict__ de la clase)

def saludar(self):
    print('Saludando...')

MiNuevaClase = type('MiNuevaClase', (object,), {'idioma':'Español','saludar':saludar})

instancia = MiNuevaClase()
print(instancia.idioma)
instancia.saludar()

# Crear una clase Videojuego, que tenga constructor con título y plataforma, y método mostrar datos
# que muestre todos los datos.
# Instanciamos un objeto y lo usamos

def inicializador(self, titulo, plataforma):
    self.titulo = titulo
    self.plataforma = plataforma

def mostrar_datos(self):
    # Alternativa 'manual'
    print(f'Título:{self.titulo}. Plataforma:{self.plataforma}')
    # Alternativa 'automática' (Jacobo)
    # for attr in self.__dict__:
    #     print(f"Atributo {attr}: {self.__dict__[attr]}")

# El método __str__ se agrega como una función lambda (idea de Bernardo)
Videojuego = type(
    'Videojuego',
    (object,),
    {'__init__':inicializador, 
     'mostrar_datos': mostrar_datos, 
     '__str__': lambda self : f'*{self.titulo}*{self.plataforma}*'})

cod = Videojuego('Call of Duty', 'XBox Series S')
cod.mostrar_datos()
print('Título:', cod.titulo)
print(cod) # *Call of Duty*XBox Series S*