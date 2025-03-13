def decorador(idioma):
    def external_wrapper(funcion):
        def internal_wrapper(*args, **kwargs):
            if (idioma=='es'):
                print('En español')
            elif (idioma=='en'):
                print('En inglés')
            resultado = funcion(*args, **kwargs)
            return resultado
        return internal_wrapper
    return external_wrapper

@decorador('en')
def calcular_suma(sumando_1, sumando_2):
    return sumando_1 + sumando_2

resultado = calcular_suma(8, 4)
print(f'El resultado es {resultado}')