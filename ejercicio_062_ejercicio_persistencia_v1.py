'''
Mostrar un menú con las siguientes opciones:
1. Añadir Película (pide datos y los guarda)
2. Recuperar Película (pide título, la recupera y la muestra)
3. Salir
Nota: utilizamos el módulo pickle
'''

from ejercicio_062_persistencia import GestorPersistenciaFactory

class Pelicula:
    gestor_persistencia = GestorPersistenciaFactory.get_gestor_persistencia()
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

    def __str__(self):
        return f'Título:{self.titulo}. Director:{self.director}'
    
    def __repr__(self):
        return f'Título:{self.titulo}. Director:{self.director}'

    def create(self):
        Pelicula.gestor_persistencia.create(self.titulo, self)

    @classmethod
    def read(cls, titulo):
        return cls.gestor_persistencia.read(titulo)


if __name__=='__main__':
    while (True):
        print('1. Añadir Peli')
        print('2. Recuperar Peli')
        print('3. Salir')
        opcion = int(input('Introduce una opción (1-3):'))
        match opcion:
            case 1:
                titulo = input('Título:')
                director = input('Director:')
                nueva_pelicula = Pelicula(titulo, director)
                nueva_pelicula.create()
            case 2:
                titulo = input('Titulo:')
                pelicula_recuperada = Pelicula.read(titulo)
                print(pelicula_recuperada)
            case 3:
                break
            case _:
                print('Opción no existente')