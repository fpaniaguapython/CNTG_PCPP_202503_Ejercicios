# Impedir que la clase Película admita más atributos de los que se crean en el __init__.

# Solución de Sonia
# class Pelicula:
#     def __init__(self, titulo, duracion):
#         super().__setattr__('titulo', titulo)
#         super().__setattr__('duracion', duracion)

#     def __getattribute__(self, name):
#         return super().__getattribute__(name)

#     def __setattr__(self, name, value):
#         if not hasattr(self, name):
#             raise AttributeError('No se pueden añadir nuevos atributos')
#         super().__setattr__(name, value)

# p = Pelicula('El Padrino', 175)
# print(p.titulo)
# # p.genero = 'Drama' # Provoca error

# Solución de clase
class Pelicula:
    def __init__(self, titulo, duracion):
        self.__bloqueado = False # __ renombra el atributo a _Pelicula__bloqueado
        self.titulo = titulo
        self.duracion = duracion
        self.__bloqueado = True

    def __getattribute__(self, name):
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if not hasattr(self, '_Pelicula__bloqueado'):
            print('1')
            super().__setattr__(name, value)
        elif not self.__bloqueado:
            print('2:', name)
            super().__setattr__(name, value)
        elif hasattr(self, name):
            print('3:', name)
            super().__setattr__(name, value)
        else:
            print('4')
            raise AttributeError("No admiten atributos no definidos")
        
p = Pelicula('El Padrino', 175)
p.titulo = 'La Madrina'
# p.director = 'Francisco' # Produce un error 

# Solución ChatGPT (No nos gusta mucho)
# class Película:
#     def __init__(self, título, director, año):
#         self._atributos_permitidos = {'título', 'director', 'año'}
#         self.título = título
#         self.director = director
#         self.año = año
#     def __setattr__(self, name, value):
#     # Permite establecer solo atributos en el conjunto de atributos permitidos
#         if name in self._atributos_permitidos:
#             super().__setattr__(name, value)
#         else:
#             raise AttributeError(f"No se permite establecer el atributo '{name}'")