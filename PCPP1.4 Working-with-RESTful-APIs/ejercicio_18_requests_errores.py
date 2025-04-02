import requests 

try:
    reply = requests.get('http://localhost:3000/', timeout=0.1)
except requests.exceptions.InvalidURL as iurl:
    # La URL Está mal construida
    print('*InvalidURL:', iurl)
except requests.exceptions.Timeout as to:
    # Error de timeout (capturar antes que ConnectionError)
    print('*Timeout:', to)
except requests.exceptions.ConnectionError as ce:
    # Error de conexión
    print('*ConnectionError:', ce)
else:
    print(reply.status_code)