import json

# Función dumps: convierte un objeto a json (no siempre)
# Función dump: convierte un objeto a json (no siempre) y lo almacena en un fichero

texto = "Este texto es normal"
print(json.dumps(texto)) # "Este texto es normal"

texto = "Este texto no es \"normal\""
print(json.dumps(texto)) # "Este texto no es \"normal\""

numero = 1_900
print(json.dumps(numero)) # 1900

diccionario = {'nombre' : 'Python', 'tipo': 'Multiparadigma'}
print(json.dumps(diccionario)) # {"nombre": "Python", "tipo": "Multiparadigma"}

tupla = ("Primavera", "Verano", "Otoño", "Invierno")
print(json.dumps(tupla)) # ["Primavera", "Verano", "Oto\u00f1o", "Invierno"]

precio_justo = True 
print(json.dumps(precio_justo)) # true

valor = None
print(json.dumps(valor)) # null


