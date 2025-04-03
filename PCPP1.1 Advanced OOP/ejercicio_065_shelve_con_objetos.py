'''
Utilizando shelve crear un sistema de almacenamiento de objetos Libro
utilizando como clave el ISBN.
'''
# 9788423367177, Las fuerzas contrarias, Lorenzo Silva
# 9788401034794, El albatros negro, María Oruña 
# 9788410140196, Fundido a negro, Jesús Cañadas

import shelve

class Libro:
    def __init__(self, isbn, titulo, autor):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f'{self.isbn}, {self.titulo}, {self.autor}'

libro_1 = Libro('9788423367177', 'Las fuerzas contrarias', 'Lorenzo Silva')
libro_2 = Libro('9788401034794', 'El albatros negro', 'María Oruña')
libro_3 = Libro('9788410140196', 'Fundido a negro', 'Jesús Cañadas')

fichero_libros = shelve.open('libros.shlv', flag='c')

# Escritura
fichero_libros[libro_1.isbn]=libro_1
fichero_libros[libro_2.isbn]=libro_2
fichero_libros[libro_3.isbn]=libro_3

# Lectura
el_albatros_negro = fichero_libros['9788401034794']
print(type(el_albatros_negro))
print(el_albatros_negro)

# Obtención del número de elementos
print(f'Tengo {len(fichero_libros)} libros')

# Borrado de elementos
del fichero_libros['9788401034794']

# Sincronización de datos (vaciado del buffer)
fichero_libros.sync() # Sincroniza la estructa de datos en memoria con el fichero

# Obtención del número de elementos (función len)
print(f'Tengo {len(fichero_libros)} libros')

# Lectura de un elemento inexistente (operador in)
if '9788401034794' in fichero_libros.keys():
    mi_libro = fichero_libros['9788401034794']
    print(mi_libro)
else:
    print('No tenemos ese libro en stock')

# Actualización masiva con update
fichero_libros.update({'DESCONOCIDO 1':'Libro desconocido', 'DESCONOCIDO 2': 'Otro libro desconocido'})

# Obtención del número de elementos
print(f'Tengo {len(fichero_libros)} libros')
for isbn in fichero_libros.keys():
    print(isbn)

# Cierre
fichero_libros.close()