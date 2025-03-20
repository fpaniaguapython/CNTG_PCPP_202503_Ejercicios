class MiMetaclase(type):
    def __new__(msc, name, bases, dictionary):
        print('msc:', msc) # msc: <class '__main__.MiMetaclase'>
        print('name:', name) # name: MiClase
        print('bases:', bases) # ()
        print('dictionary:', dictionary) # dictionary: {'__module__': '__main__', '__qualname__': 'MiClase', '__firstlineno__': 12, 'mostrar': <function MiClase.mostrar at 0x000001D0A95439C0>, '__static_attributes__': ()}
        obj = super().__new__(msc, name, bases, dictionary)
        obj.nuevo_atributo = 'Añadido por la metaclase' # Atributo de clase
        obj.metodo = lambda : 'Hola' # Método de clase
        return obj

class MiClase(metaclass=MiMetaclase):
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar(self):
        print('Soy el método mostrar...')

mi_objeto = MiClase('Python')
print(MiClase.metodo())
print('MiClase.__name__:', MiClase.__name__) # MiClase
print('MiClase.__bases__:', MiClase.__bases__) # (<class 'object'>,)
print('MiClase.__dict__:', MiClase.__dict__) # (entre otras cosas): 'nuevo_atributo': 'Añadido por la metaclase'
print('mi_objeto.__dict__:', mi_objeto.__dict__) # mi_objeto.__dict__: {'nombre': 'Python'}