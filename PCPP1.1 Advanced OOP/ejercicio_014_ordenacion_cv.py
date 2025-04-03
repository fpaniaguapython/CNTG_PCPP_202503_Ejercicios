'''
Ordenar los candidatos según este cálculo:
Año de experiencia - 1 punto
Inglés - 3 puntos
Japonés - 5 puntos
'''

class Candidato:
    def __init__(self, nombre, experiencia : int, ingles : bool, japones : bool):
        self.nombre = nombre
        self.experiencia = experiencia
        self.ingles = ingles
        self.japones = japones

    def __repr__(self):
        return self.nombre


c1 = Candidato('Juan', 5, True, False)
c2 = Candidato('Rosa', 4, True, True)
c3 = Candidato('Anna', 10, False, False)
c4 = Candidato('Ricardo', 2, False, True)

# Solución con función externa (versión Fernando)
candidatos = [c1, c2, c3, c4]
def valorar_candidato(candidato : Candidato):
    PUNTUACION_EXPERIENCIA = 1
    PUNTUACION_INGLES = 3
    PUNTUACION_JAPONES = 5
    puntos = candidato.experiencia * PUNTUACION_EXPERIENCIA
    # If tradicional
    if candidato.ingles:
        puntos += PUNTUACION_INGLES
    # Expresión ternaria
    puntos += PUNTUACION_JAPONES if candidato.japones else 0 
    return puntos

candidatos.sort(key=valorar_candidato, reverse=True)
print(candidatos) # [Rosa, Anna, Juan, Ricardo]

# Solución con función lambda (versión Sonia)
candidatos = [c1, c2, c3, c4]
PUNTUACION_EXPERIENCIA = 1
PUNTUACION_INGLES = 3
PUNTUACION_JAPONES = 5
candidatos.sort(key=lambda candidato: 
                candidato.experiencia  * PUNTUACION_EXPERIENCIA
                + (PUNTUACION_INGLES if candidato.ingles else 0) 
                + (PUNTUACION_JAPONES if candidato.japones else 0), 
                reverse=True)
print(candidatos) # [Rosa, Anna, Juan, Ricardo]

# Solución con función lambda (versión Souto)
candidatos = [c1, c2, c3, c4]
PUNTUACION_EXPERIENCIA = 1
PUNTUACION_INGLES = 3
PUNTUACION_JAPONES = 5
candidatos.sort(key=lambda candidato: 
                candidato.experiencia * PUNTUACION_EXPERIENCIA + 
                PUNTUACION_INGLES * candidato.ingles + 
                PUNTUACION_JAPONES * candidato.japones, 
                reverse=True)
print(candidatos) # [Rosa, Anna, Juan, Ricardo]