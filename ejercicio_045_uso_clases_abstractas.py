import abc


class Notificador(abc.ABC):
    def mostrar_info(self):
        print('Mostrando info...')

    @abc.abstractmethod
    def notificar(self, destinatario, mensaje):
        pass

class NotificadorEmail(Notificador):
    def notificar(self, destinatario, mensaje):
        print(f'Enviando un email a {destinatario} con el mensaje {mensaje}')

class NotificadorConPaloma(Notificador):
    def notificar(self, destinatario, mensaje):
        print(f'Enviando una paloma mensajera a {destinatario} con el mensaje {mensaje}')

class NotificadorConWhatsapp(Notificador):
    def notificar(self, destinatario, mensaje):
        print(f'Enviando un whatsapp a {destinatario} con el mensaje {mensaje}')

def get_notificator():
    return NotificadorConWhatsapp()

# ***********************************************************************************************

notificaciones = (('Víctor','Tienes que ver Sharknado'),('Souto','Tienes que ver El Resplandor'))
notificador = get_notificator()
if (isinstance(notificador, Notificador)):
    notificador.mostrar_info()
    for notificacion in notificaciones:
        notificador.notificar(notificacion[0], notificacion[1])
else:
    raise TypeError('El notificador es un fake')