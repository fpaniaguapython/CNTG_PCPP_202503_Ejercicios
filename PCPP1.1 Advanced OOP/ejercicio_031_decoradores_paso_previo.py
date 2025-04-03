def decorador_simple(funcion):
    print('Soy la decoración')
    return funcion

def saludador():
    print('Hola, soy un saludador')

funcion_decorada = decorador_simple(saludador)
funcion_decorada()


