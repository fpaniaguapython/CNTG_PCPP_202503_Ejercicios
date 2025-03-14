class Pelicula:
    def __init__(self, titulo):
        self.titulo = titulo

class ListaPeliculas(list):
    clase = Pelicula
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def append(self, object):
        if (not isinstance(object,Pelicula)):
            raise TypeError('No es una película')
        super().append(object)


peliculas = ListaPeliculas()
peliculas.append(Pelicula('El Resplandor'))
peliculas.append(Pelicula('Sharknado'))
peliculas.append(Pelicula('El ataque del tiburón de 3 cabezas'))
peliculas.append('Melón') # Error
print(peliculas)
