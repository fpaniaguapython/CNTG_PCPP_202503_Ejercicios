# Decorador con función y argumentos
def decorador(argumento):
    def funcion_externa(funcion):
        def funcion_interna(*args, **kwargs):
            if (argumento==True):
                print('Decorando...')
            else:
                print('No decorando...')
            return funcion(*args, **kwargs)
        return funcion_interna
    return funcion_externa

# Decorador con función y argumentos
class ClaseDecoradora:
    def __init__(self, argumento):
        self.argumento = argumento

    def __call__(self, funcion_a_decorar):
        def funcion_interna(*args, **kwargs):
            if (self.argumento==True):
                print('Decorando...')
            else:
                print('No decorando...')
            return funcion_a_decorar(*args, **kwargs)
        return funcion_interna

@ClaseDecoradora(True)
def saludar():
    print('Hola')

saludar()