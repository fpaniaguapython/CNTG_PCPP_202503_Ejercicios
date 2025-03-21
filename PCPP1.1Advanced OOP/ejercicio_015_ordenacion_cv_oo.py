'''
Ordenar los candidatos según este cálculo:
Año de experiencia - 1 punto
Inglés - 3 puntos
Japonés - 5 puntos
'''
class Candidato:
    PUNTUACION_EXPERIENCIA = 1
    PUNTUACION_INGLES = 3
    PUNTUACION_JAPONES = 5
    def __init__(self, nombre, experiencia : int, ingles : bool, japones : bool):
        self.nombre = nombre
        self.experiencia = experiencia
        self.ingles = ingles
        self.japones = japones

    def __repr__(self):
        return self.nombre
    
    def valorar_candidato(self):
        puntos = self.experiencia * Candidato.PUNTUACION_EXPERIENCIA
        # If tradicional
        if self.ingles:
            puntos += Candidato.PUNTUACION_INGLES
        # Expresión ternaria
        puntos += Candidato.PUNTUACION_JAPONES if self.japones else 0 
        return puntos

c1 = Candidato('Juan', 5, True, False)
c2 = Candidato('Rosa', 4, True, True)
c3 = Candidato('Anna', 10, False, False)
c4 = Candidato('Ricardo', 2, False, True)

candidatos = [c1, c2, c3, c4]

candidatos.sort(key=Candidato.valorar_candidato, reverse=True)
print(candidatos) # [Rosa, Anna, Juan, Ricardo]