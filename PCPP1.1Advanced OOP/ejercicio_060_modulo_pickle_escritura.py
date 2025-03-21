import pickle

class Pelicula:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

    def get_director(self):
        return self.director
    
    def __str__(self):
        return f'Título:{self.titulo}. Director:{self.director}'

alien = Pelicula('Alien', 'Ridley Scott')

with open('pelicula.pickle',mode='wb') as fichero_peliculas:
    pickle.dump(obj=alien, file=fichero_peliculas)