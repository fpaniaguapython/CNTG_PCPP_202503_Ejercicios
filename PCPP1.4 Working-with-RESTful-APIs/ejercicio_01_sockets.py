#
# Pasos para crear un client-socket:
#
# 1. Crear el socket: clase socket
# 2. Establecer la conexión: método connect
# 3. Enviar la solicitud: método send
# 4. Recibir la respuesta: método recv
# 5. Cerrar el socket: métodos shutdown y close.

# Nota: para ejecutar el ejemplo se debe arrancar
# un servidor web ejecutando:
# python -m http.server 
# en cualquier carpeta


import socket

server_addr = input('Host IP:') # Indicar localhost
server_port = int(input('Host Port:')) # Indicar 8000

# 1. Crear el socket: clase socket
# AF_INET --> Socket se basa en DIRECCION + PUERTO
# SOCK_STREAM --> Socket de tipo TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Establecer la conexión: método connect
sock.connect((server_addr, server_port))  # OJO, ES UNA TUPLA

# 3. Enviar la solicitud: método send
sock.send(b"GET / HTTP/1.1\r\nHost: " +
            bytes(server_addr, "utf8") +
            b"\r\nConnection: close\r\n\r\n")

# 4. Recibir la respuesta: método recv
# El argumento de recv es el tamaño del buffer de bytes
respuesta = sock.recv(1000)

# 5. Cerrar el socket: métodos shutdown y close.
# Las constances de shutdown son:
# SHUT_RDWR --> Dejamos de leer y escribir
# SHUT_RD --> Dejamos de leer
# SHUT_WR --> Dejamos de escribir
sock.shutdown(socket.SHUT_RDWR)
sock.close()

# Tratar la respuesta
print(repr(respuesta))