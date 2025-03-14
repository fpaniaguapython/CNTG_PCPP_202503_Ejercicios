# Hacer un decorador para incorporar a cualquier clase
# un método que 'envíe' la información de los atributos del objeto
# Podemos llamar al método enviar_info

# Versión José Luis
def funcion_enviar_info(self):
    print("Enviando información de:", self.__class__.__name__)
    for k,v in self.__dict__.items():
        print(k,":\t",v)  
    print("Enviado")  


def enviador_email(clase_a_decorar):
    clase_a_decorar.enviar_info = funcion_enviar_info
    return clase_a_decorar

@enviador_email
class Factura:
    def __init__(self, numero, importe):
        self.numero = numero
        self.importe = importe
    
    def mostrar_numero(self):
        print('Número:',self.numero)

@enviador_email
class Persona:
    def __init__(self, nombre, apellidos, email):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

f1 = Factura(1, 100)
f1.enviar_info()
f1.mostrar_numero()
print(Factura.__dict__)

p1 = Persona('Fernando', 'Paniagua', 'fernando@gmail.com')
p1.enviar_info()