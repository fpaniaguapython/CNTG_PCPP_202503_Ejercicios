import pickle 

class Pelicula:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

    def get_director(self):
        return self.director
    
    def __str__(self):
        return f'Título:{self.titulo}. Director:{self.director}'

with open('pelicula.pickle',mode='rb') as fichero_peliculas:
    pelicula = pickle.load(file=fichero_peliculas)

print(pelicula)