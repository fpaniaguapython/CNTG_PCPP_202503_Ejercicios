def asteriscador(funcion_a_decorar):
    def funcion_interna(*args, **kwargs):
        print('*'*len(args[0]))
        retorno = funcion_a_decorar(*args, **kwargs)
        print('*'*len(args[0]))
        return retorno
    return funcion_interna

@asteriscador
def mostrar_en_mayusculas(texto: str):
    print(texto.upper())
    return len(texto)>10


mayor_10 = mostrar_en_mayusculas('Me gusta Python')
print(mayor_10)
