# Se intercambian mensajes introducidos por el usuario
# hasta que se escriba la palabra VAIVAI

import socket

HOST_IP = '127.0.0.1'
HOST_PORT = 8021
EXIT_STRING = 'VAIVAI'

# Creamos el scoket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Indicamos IP y port
sock.connect((HOST_IP, HOST_PORT))
while (True):
    # Envío de mensaje
    mensaje=input('Mensaje:')
    sock.send(mensaje.encode('utf-8'))
    print(f'(Cliente):{mensaje}')
    if (mensaje==EXIT_STRING):
        break
    # Lectura de mensaje
    respuesta = sock.recv(1024)
    print(f'(Servidor):{respuesta.decode('utf-8')}')
# Cierre
sock.shutdown(socket.SHUT_RDWR)
sock.close()