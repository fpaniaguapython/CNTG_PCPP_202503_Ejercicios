# Conversión a JSON de un objeto propio
# Alternativa 1 - A través de una función o método estático
import json

class Equipo:
    def __init__(self, nombre, sede):
        self.nombre = nombre
        self.sede = sede

class EquipoEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Equipo):
            return o.__dict__
        else:
            return super().default(self)
        
equipo = Equipo('Valencia C.F.', 'Valencia')
print(json.dumps(equipo, cls=EquipoEncoder)) # {"nombre": "Valencia C.F.", "sede": "Valencia"}
print(json.dumps("Lo que sea", cls=EquipoEncoder)) # "Lo que sea"