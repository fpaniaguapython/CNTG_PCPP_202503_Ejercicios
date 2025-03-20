'''
Crear un metaclase Comunicador
Las clases que se creen como consecuencia de Comunicador
deberán implementar los métodos:
enviar_email
enviar_sms
enviar_whatsapp

Además, añadir un método que se llame enviar_global
que envíe a través de todos los métodos anteriores
'''
class Comunicador(type):
    METODOS_OBLIGATORIOS = ['enviar_email','enviar_sms','enviar_whatsapp']
    def __new__(msc, name, bases, dictionary):
        for metodo in Comunicador.METODOS_OBLIGATORIOS:
            if ((metodo not in dictionary.keys()) or not callable(dictionary[metodo])):
                raise NotImplementedError(f'El método {metodo} no está implementado')
        obj = super().__new__(msc, name, bases, dictionary)
        obj.enviar_global = Comunicador.enviar_global
        return obj
    
    def enviar_global(self):
            self.enviar_email()
            self.enviar_sms()
            self.enviar_whatsapp()

class Factura(metaclass=Comunicador):
    def enviar_email(self):
        print("Enviado email")
    def enviar_sms(self):
        print("Enviado sms")
    def enviar_whatsapp(self):
        print("Enviado whatsapp")

factura = Factura()
factura.enviar_global()