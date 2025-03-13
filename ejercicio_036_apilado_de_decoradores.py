def decorador_1(funcion):
    def internal_wrapper(*args, **kwargs):
        print('Decorador 1',args)
        return funcion(*args, **kwargs)
    return internal_wrapper

def decorador_2(funcion):
    def internal_wrapper(*args, **kwargs):
        print('Decorador 2',args)
        return funcion(*args, **kwargs)
    return internal_wrapper

@decorador_2
@decorador_1
def saludar(nombre):
    return f'Hola {nombre}'

print(saludar('Diego'))

# Sólo se ejecuta la función decorada en el último paso.

'''
Decorador 2 ('Diego',)
Decorador 1 ('*args, **kwargs',)
Hola *args, **kwargs
'''
    