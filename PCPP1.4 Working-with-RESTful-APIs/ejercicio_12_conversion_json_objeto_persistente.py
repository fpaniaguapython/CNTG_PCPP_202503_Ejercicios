# Pregunta si queremos escribir o leer.
# Si es escribir, guarda el json en un fichero
# Si es leer, restaura el objeto a partir del fichero
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

opcion = int(input('Introduce una opción (1. Guardar, 2. Recuperar):'))

if (opcion==1):
    equipo = Equipo('C.D. Leganés', 'Leganés')
    with open('lega.json', 'w', encoding='utf-8') as fichero:
        equipo_json = json.dump(equipo, fichero, default=encoder_equipo, ensure_ascii=False)
    print('¡Guardado!')
else:
    with open('lega.json', 'r', encoding='utf-8') as fichero:
        nuevo_equipo = json.load(fichero, object_hook=decoder_equipo)
    print(type(nuevo_equipo)) # <class '__main__.Equipo'>
    print(nuevo_equipo.nombre) # C.D. Leganés