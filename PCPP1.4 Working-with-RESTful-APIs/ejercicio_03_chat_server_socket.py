# Se intercambian mensajes introducidos por el usuario
# hasta que se reciba la palabra VAIVAI

import socket

host = '127.0.0.1' # direccion del servidor (127.0.0.1 = localhost)
port = 8021 # el puerto de escucha

# Creación del socket
sock_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asignar servidor y puerto al socket
sock_servidor.bind((host, port))

# Indicar al socket-server que quede a la escucha
sock_servidor.listen()
print(f'Servidor {host} escuchando en el puerto {port}')

# Indicar al socket-server que recibas los paquetes de datos
socket_cliente, direccion_cliente = sock_servidor.accept()
print(f'Se ha recibido una petición desde {direccion_cliente}')

# Recoger los datos
datos = socket_cliente.recv(1024)
print(f'Datos recibidos del cliente: "{datos.decode('utf-8')}"')

# Envió de la respuesta
mensaje = 'Hola, soy el servidor'
socket_cliente.send(mensaje.encode('utf-8'))
print(f'Se ha enviado al cliente el siguiente mensaje "{mensaje}"')

socket_cliente.close()
sock_servidor.close()






