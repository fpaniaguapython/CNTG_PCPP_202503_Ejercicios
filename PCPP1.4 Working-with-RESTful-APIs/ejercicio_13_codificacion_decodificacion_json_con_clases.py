import json

class Equipo:
    def __init__(self, nombre, sede):
        self.nombre = nombre
        self.sede = sede

# json.JSONEncoder
class EquipoEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Equipo):
            return o.__dict__
        else:
            return super().default(self)
        
# json.JSONDecoder
class EquipoDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decoder)

    def decoder(self, equipo_json):
        # return Equipo(**equipo_json)
        return Equipo(nombre=equipo_json['nombre'], sede=equipo_json['sede'])
        
# Transformacion a JSON
equipo = Equipo('Valencia C.F.', 'Valencia')
equipo_json = json.dumps(equipo, cls=EquipoEncoder)
print(equipo_json) # {"nombre": "Valencia C.F.", "sede": "Valencia"}

# Transformacion a Objeto Python
nuevo_equipo = json.loads(equipo_json, cls=EquipoDecoder)
print(type(nuevo_equipo)) # Equipo
print(nuevo_equipo.nombre) # Valencia C.F.