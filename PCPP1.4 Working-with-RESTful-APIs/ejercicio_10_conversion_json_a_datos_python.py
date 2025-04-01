import json

entrada = '3.1416'
dato = json.loads(entrada)
print(type(dato)) # <class 'float'>
print(dato) # 3.1416

entrada = '24'
dato = json.loads(entrada)
print(type(dato)) # <class 'int'>
print(dato) # 24

entrada = 'true'
dato = json.loads(entrada)
print(type(dato)) # <class 'bool'>
print(dato) # True

entrada = '"Lo que sea"'
dato = json.loads(entrada)
print(type(dato)) # <class 'str'>
print(dato) # "Lo que sea"

entrada = '[1, 2, 3]'
dato = json.loads(entrada)
print(type(dato)) # <class 'list'>
print(dato) # [1, 2, 3]

entrada = '{"nombre": "Python", "tipo": "Multiparadigma"}'
dato = json.loads(entrada)
print(type(dato)) # <class 'dict'>
print(dato) # {'nombre': 'Python', 'tipo': 'Multiparadigma'}

