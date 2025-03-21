# Implementación a través de un factory
class Traductor:
    def __init__(self):
        print('__init__ de Traductor')

class TraductorFactory:
    __instancia = None
    @classmethod
    def get_traductor(cls):
        if (cls.__instancia==None):
            cls.__instancia = Traductor()
        return cls.__instancia

traductor_1 = TraductorFactory.get_traductor()
traductor_2 = TraductorFactory.get_traductor()
traductor_3 = TraductorFactory.get_traductor()

print(id(traductor_1))
print(id(traductor_2))
print(id(traductor_3))

# Implementación de un singleton a través del método __new__
class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance
  
singleton = SingletonClass()
new_singleton = SingletonClass()

print(singleton is new_singleton)

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)