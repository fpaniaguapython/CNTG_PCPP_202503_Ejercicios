# Conversión a JSON de un objeto propio
# Alternativa 1 - A través de una función o método estático
import json

class Equipo:
    def __init__(self, nombre, sede):
        self.nombre = nombre
        self.sede = sede

    # Solución con método estático
    # @staticmethod
    # def encoder(equipo):
    #     if isinstance(equipo, Equipo):
    #         return equipo.__dict__
    #     else:
    #         raise TypeError('No es serializable')

# Solución con función
def encoder_equipo(equipo):
    if isinstance(equipo, Equipo):
        return equipo.__dict__
    else:
        raise TypeError('No es serializable') 

equipo = Equipo('C.D. Leganés', 'Leganés')

# Solución con __dict__
# print(json.dumps(equipo.__dict__)) # Opción más 'simple'

# Solución con método estático
# print(json.dumps(equipo, default=Equipo.encoder)) # default determina la función para obtener algo 

# Solución con función
# ensure_ascii=False --> No escapa los caracteres no ascii
print(json.dumps(equipo, default=encoder_equipo, ensure_ascii=False))
# Con ensure_ascii por defecto (True): {"nombre": "C.D. Legan\u00e9s", "sede": "Legan\u00e9s"}
# Con ensure_ascii=False {"nombre": "C.D. Leganés", "sede": "Leganés"}