# La clase Tarea tiene dos atributos y un método
# ejecutar() que imprime un mensaje. 
class Tarea:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def ejecutar(self):
        print('Ejecutando la tarea:', self.nombre)

# La función ejecutador recibe una tarea y la ejecuta.
# Confirmar que se recibe una Tarea.
# Confirmar que la tarea se puede ejecutar.
# Si algo está mal, lanzar una excepción.
def ejecutador(tarea: Tarea) -> None:
    if (not isinstance(tarea, Tarea)):
        raise TypeError('Se esperaba un objeto de tipo Tarea')
    if (not hasattr(tarea, 'ejecutar')):
        raise AttributeError('No dispone del método ejecutar')
    if (not callable(getattr(tarea, 'ejecutar'))):
        raise AttributeError('El método ejecutar no es callable')
    tarea.ejecutar()

tarea = Tarea('Limpiar', 'Limpiar la casa')
try:
    # ejecutador('Pollo de goma') # Genera la excepción TypeError
    # delattr(Tarea, 'ejecutar') # El método se elimina DE LA CLASE. Genera la excepción AttributeError
    # tarea.ejecutar = 'Otra cosa' # Genera una excepción AttributeError
    ejecutador(tarea)
except TypeError as te:
    print('TypeError:', te)
except AttributeError as ae:
    print('AttributeError:', ae)