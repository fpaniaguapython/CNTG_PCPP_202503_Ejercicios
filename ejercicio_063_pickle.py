import pickle

# Serialización y almacenamiento de una funcion (lo mismo para las clases)

def saludar():
    print('Hola')

with open('funcion.pickle', 'wb') as fichero:
    pickle.dump(saludar, fichero) # Solo almacena la referencia a la función

with open('funcion.pickle', 'rb') as fichero:
    mi_funcion = pickle.load(fichero) # # Solo recupera la referencia a la función

print(type(mi_funcion)) 
mi_funcion() # Funciona porque la función 'saludar' está en memoria



