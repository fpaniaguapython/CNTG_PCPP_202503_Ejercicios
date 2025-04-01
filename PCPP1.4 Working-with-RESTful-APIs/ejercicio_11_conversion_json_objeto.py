import json

class Equipo:
    def __init__(self, nombre, sede):
        self.nombre = nombre
        self.sede = sede

# Transformar el equipo a algo compatible con json
def encoder_equipo(equipo):
    if isinstance(equipo, Equipo):
        return equipo.__dict__
    else:
        raise TypeError('No es serializable')
    
# Transformar el objeto json a objeto equipo
def decoder_equipo(equipo_json):
    return Equipo(equipo_json['nombre'], equipo_json['sede'])

# 1. Creamos el equipo
equipo = Equipo('C.D. Leganés', 'Leganés')
# 2. Convertimos a JSON
equipo_json = json.dumps(equipo, default=encoder_equipo)
# 3. Convertir el objeto JSON a objeto Python
nuevo_equipo = json.loads(equipo_json, object_hook=decoder_equipo)
# 4. nuevo_equipo es una instancia de Equipo
print(type(nuevo_equipo)) # <class '__main__.Equipo'>
print(nuevo_equipo.nombre) # C.D. Leganés