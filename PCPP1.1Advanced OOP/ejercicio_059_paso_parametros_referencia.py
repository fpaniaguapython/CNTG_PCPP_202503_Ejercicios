# - Clase Pelicula con dos atributos
# - Creamos una función SIN RETORNO que recibe un objeto Pelicula y modifica 
# alguno de sus atributos.
# - Creamos una instancia de Película, la pasamos como argumento a la función
# y la modificamos dentro de esta. ¿Se modifica el objeto fuera de la función?

def modificar_pelicula(pelicula):
    pelicula.titulo = pelicula.titulo.upper()

class Pelicula:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director
    
    def __str__(self):
        return f'Título:{self.titulo}. Director:{self.director}'

pelicula_1 = Pelicula('pelicula 1', 'director 1')
modificar_pelicula(pelicula=pelicula_1) # Paso de parámetros por referencia
print(pelicula_1) # Título:PELICULA 1. Director:director 1