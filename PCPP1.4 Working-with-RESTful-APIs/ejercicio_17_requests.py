# pip install requests

import requests 

reply = requests.get('http://localhost:3000/') # Petición GET
# **************************************
# CÓDIGO DE CONTROL DE HTTP: status_code
# **************************************
status_code = reply.status_code # Código HTTP de la respuesta

if (status_code==200):
    print('OK')

if (status_code==requests.codes.OK):
    print('OK')

if (status_code==requests.codes.ok):
    print('OK')

if (status_code==requests.codes.okay):
    print('OK')

# **************************************
# CÓDIGO DE CONTROL DE HTTP: response
# **************************************
response = reply.text
print(response)