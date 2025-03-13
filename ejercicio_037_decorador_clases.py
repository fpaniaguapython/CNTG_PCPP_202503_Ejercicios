def decorador(funcion):
    def funcion_interna(*args, **kwargs):
        print('Decorando...')
        return funcion(*args, **kwargs)
    return funcion_interna

class ClaseDecoradora:
    def __init__(self, funcion_a_decorar):
        self.funcion_a_decorar = funcion_a_decorar

    def __call__(self, *args, **kwds):
        print('Ejecutando ClaseDecoradora...')
        self.funcion_a_decorar()
        print('Fin de la decoración...')

@ClaseDecoradora
def saludar():
    print('Hola')

saludar()

VUELTA A LAS 18:45