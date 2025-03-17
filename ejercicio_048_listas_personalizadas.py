class Pelicula:
    def __init__(self, titulo):
        self.titulo = titulo
    def __repr__(self):
        return f'Título:{self.titulo}'

class ListaPeliculas(list):
    __clase = Pelicula
    def __init__(self, *args, **kwargs):
        print('__init__')
        for object in args[0]:
            if (not isinstance(object, ListaPeliculas.__clase)):
                raise TypeError('No es una película')
        super().__init__(*args, **kwargs)

    def append(self, object):
        print('append')
        if (not isinstance(object, ListaPeliculas.__clase)):
            raise TypeError('No es una película')
        super().append(object)

    def __setitem__(self, index, object):
        print('__setitem__')
        if (not isinstance(object, ListaPeliculas.__clase)):
            raise TypeError('No es una película')
        super().__setitem__(index, object)

    def insert(self, index, object):
        print('insert')
        if (not isinstance(object, ListaPeliculas.__clase)):
            raise TypeError('No es una película')
        super().insert(index, object)



# Construcción de una lista a partir de un iterable
# peliculas = ListaPeliculas((1,2,3)) # Error
peliculas = ListaPeliculas((Pelicula('Spiderman'), Pelicula('Superman')))

# Construcción de una lista vacía
# peliculas = ListaPeliculas()

# Acceso con append
peliculas.append(Pelicula('El Resplandor'))
peliculas.append(Pelicula('Sharknado'))
# peliculas.append('Melón') # Error

# Acceso por índice
# peliculas[0]='Melón' # Error
peliculas[0]=Pelicula('El ataque del tiburón de 3 cabezas')

# Acceso con insert
# peliculas.insert(1,'Sandía') # Error
peliculas.insert(1, Pelicula('Memorías de África'))



print(peliculas)
