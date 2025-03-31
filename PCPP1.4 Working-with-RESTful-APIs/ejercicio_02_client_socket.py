import socket

HOST_IP = '127.0.0.1'
HOST_PORT = 8021

# Creamos el scoket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Indicamos IP y port
sock.connect((HOST_IP, HOST_PORT))
# Envío de mensaje
mensaje='Hola, soy el cliente'
sock.send(mensaje.encode('utf-8'))
print(f'Enviado al servidor el mensaje "{mensaje}"')
# Lectura de mensaje
respuesta = sock.recv(1024)
print(f'Recibiendo el mensaje del servidor "{respuesta.decode('utf-8')}"')
# Cierre
sock.shutdown(socket.SHUT_RDWR)
sock.close()