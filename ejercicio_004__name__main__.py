import ejercicio_005__name__main__

# La variable __name__ toma el valor __main__
# si el script es el script principal
# si no, toma el valor del nombre del módulo (script)

print('Estoy en el 4:', __name__)

if __name__=='__main__':
    print('Soy el programa principal')