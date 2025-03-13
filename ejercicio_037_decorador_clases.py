# Decorador con función
def decorador(funcion_a_decorar):
    def funcion_interna(*args, **kwargs):
        print('Decorando...')
        return funcion_a_decorar(*args, **kwargs)
    return funcion_interna

# Decorador con clase
class ClaseDecoradora:
    def __init__(self, funcion_a_decorar):
        self.funcion_a_decorar = funcion_a_decorar

    def __call__(self, *args, **kwargs):
        print('Ejecutando ClaseDecoradora...')
        self.funcion_a_decorar(*args, **kwargs)
        print('Fin de la decoración...')

@ClaseDecoradora
def saludar():
    print('Hola')

saludar()