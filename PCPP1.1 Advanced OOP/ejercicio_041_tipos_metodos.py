class Metagrupo:
    super_capacidad_maxima = 100 # Variable o atributo de clase

class Grupo(Metagrupo):
    capacidad_maxima = 50 # Variable o atributo de clase
    def __init__(self, nombre, url):
        self.nombre = nombre # Variable o atributo de instancia
        self.url = url

    def mostrar_nombre(self): # Método de instancia
        print(self.nombre)

    @classmethod
    def duplicar_capacidad(cls): # Método de clase
        cls.capacidad_maxima*=2

    @staticmethod
    def get_informacion():
        print('Un Grupo es un conjunto de personas con interes comunes')

python_corunya = Grupo('Comunidade de Python de A Coruña', 'https://linktr.ee/pythoncoruna')  

# Invocación a un método de instancia
python_corunya.mostrar_nombre()

# Invocación a un método de clase
print(Grupo.capacidad_maxima) # 50
Grupo.duplicar_capacidad()
print(Grupo.capacidad_maxima) # 100

# Invocación a un método estático
Grupo.get_informacion()