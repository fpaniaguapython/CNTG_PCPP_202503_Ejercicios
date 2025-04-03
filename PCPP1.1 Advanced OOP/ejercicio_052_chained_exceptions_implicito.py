lista = ['Ítem 1', 'Ítem 2']

try:
    print(lista[2])
except IndexError as ie:
    try:
        resultado = 10/0
    except ZeroDivisionError as zde:
        print('Exception interna (zde):', zde)
        print('Exception externa (ie):', ie)
        print('Contexto:', zde.__context__) # __context contiene la excepción externa (ie)
        print('¿ie es el mismo objeto que zde.__context__?', zde.__context__ is ie) # True