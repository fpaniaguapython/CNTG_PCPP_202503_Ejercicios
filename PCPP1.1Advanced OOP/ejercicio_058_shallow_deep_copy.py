# Tipo primitivo, copia por valor

numero_1 = 10
numero_2 = numero_1 # Realiza una copia del valor

numero_1 = 20
print(numero_1) # 20
print(numero_2) # 10

# Estructura de datos, copia por referencia

lista_1 = [10, 20, 30]
lista_2 = lista_1 # Realiza una copia del referencia

lista_1.append(40)
print(lista_1) # [10, 20, 30, 40]
print(lista_2) # [10, 20, 30, 40]

# Estructura de datos, (shallow) copia por valor utilizando slicing

lista_1 = [10, 20, 30]
lista_2 = lista_1[:] # Copia por valor

lista_1.append(40)
print(lista_1) # [10, 20, 30, 40]
print(lista_2) # [10, 20, 30]

# Estructura de datos, (shallow) copia por valor utilizando slicing

lista_1 = [10, 20, 30, [40, 50, 60]]
lista_2 = lista_1[:] # Copia por valor (pero sólo en el primer nivel)

lista_1.append(70)
print(lista_1) # [10, 20, 30, [40, 50, 60], 70]
print(lista_2) # [10, 20, 30, [40, 50, 60]]

lista_1[3].append(80)
print(lista_1) # [10, 20, 30, [40, 50, 60, 80], 70]
print(lista_2) # [10, 20, 30, [40, 50, 60, 80]]

# Estructura de datos, (deep) copia por valor utilizando el módulo copy

import copy
lista_1 = [10, 20, 30, [40, 50, 60]]
lista_2 = copy.deepcopy(lista_1) # Copia por valor en profundida
# lista_1 y lista_2 son dos objetos COMPLETAMENTE distintos

lista_1.append(70)
print(lista_1) # [10, 20, 30, [40, 50, 60], 70]
print(lista_2) # [10, 20, 30, [40, 50, 60]]

lista_1[3].append(80)
print(lista_1) # [10, 20, 30, [40, 50, 60, 80], 70]
print(lista_2) # [10, 20, 30, [40, 50, 60]]