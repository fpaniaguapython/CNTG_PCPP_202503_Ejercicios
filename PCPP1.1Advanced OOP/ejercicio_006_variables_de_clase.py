class Jugador:
    limite_salarial = 10_000

    def __init__(self, nombre, salario):
        self.nombre = nombre
        if salario > Jugador.limite_salarial:
            raise ValueError('El salario es muy alto')

try:
    ronaldo = Jugador('Ronaldo', 20_000)
    print('Fichado')
except ValueError as ve:
    print(ve) # El salario es muy alto

Jugador.limite_salarial = 20_000  

try:
    ronaldo = Jugador('Ronaldo', 20_000)
    print('Fichado')
except ValueError as ve:
    print(ve) # El salario es muy alto

print('Límite salarial:', Jugador.limite_salarial) # 20000 OK
print('Límite salarial:', ronaldo.limite_salarial) # 20000 ¿OK?
ronaldo.limite_salarial = 30_000 # Creación de un atributo de instancia K.O.
print('Límite salarial:', Jugador.limite_salarial) # 20000 OK
print('Límite salarial:', ronaldo.limite_salarial) # 30000 K.O.

print(Jugador.__dict__) # Incluye el límite salarial de la clase (atributo de Clase)
print(ronaldo.__dict__) # Incluye el límite salarial de la instancia (atributo de instancia)

iago_aspas = Jugador('Iago Aspas', 10_000)
print(iago_aspas.__dict__) # NO INCLUYE el límite salarial

iago_aspas.nonbre = 'Iago Aspas Juncal' # OJO, un error tipográfico en el nombre del atributo