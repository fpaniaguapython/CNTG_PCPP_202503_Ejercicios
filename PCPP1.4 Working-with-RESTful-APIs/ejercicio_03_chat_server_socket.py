# Se intercambian mensajes introducidos por el usuario
# hasta que se reciba la palabra VAIVAI

import socket

HOST = '127.0.0.1' # direccion del servidor (127.0.0.1 = localhost)
PORT = 8021 # el puerto de escucha
EXIT_STRING = 'VAIVAI'

# Creación del socket
sock_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asignar servidor y puerto al socket
sock_servidor.bind((HOST, PORT))

# Indicar al socket-server que quede a la escucha
sock_servidor.listen()
print(f'Servidor {HOST} escuchando en el puerto {PORT}')

# Indicar al socket-server que recibas los paquetes de datos
socket_cliente, direccion_cliente = sock_servidor.accept()
print(f'Se ha recibido una petición desde {direccion_cliente}')
while (True):
    # Recoger los datos
    print('Esperando...')
    datos = socket_cliente.recv(1024)
    datos = datos.decode('utf-8')
    print(f'(Cliente):{datos}')
    if (datos==EXIT_STRING):
        break
    # Envió de la respuesta
    mensaje = input('Mensaje de respuesta:')
    socket_cliente.send(mensaje.encode('utf-8'))
    print(f'(Servidor):{mensaje}')

socket_cliente.close()
sock_servidor.close()






