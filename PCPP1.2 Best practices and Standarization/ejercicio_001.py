# *******
# SANGRÍA
# *******

# La sangría debe ser de 4 espacios (no tabulaciones)
cantidad = 10

if cantidad > 20:
    print('Estoy a 4 espacios de la izquierda')
else:
     print('Estoy a 5 espacios de la izquierda') # No es un error sintáctico
     # Si se mezcan tabulaciones y espacios, TabError

# *******
# Líneas de continuación
# *******

# Si hay paréntesis, corchetes, o llaves
# no es necesario usar la barra invertida

if ((cantidad > 20) and 
    (cantidad < 30) and (cantidad % 2 == 0)):
     pass

# Incorrecta:
lista = [1, 2, 3,
4, 5, 6]

# Correcto:
lista = [
        1, 2, 3,
        4, 5, 6]

# *******
# Saltos de línea
# *******

# CORRECTO: Antes de los operadores binarios
total = (10
        + 20
        + 40
        + 50)

suma_totales = (5
                + 10
                + 15)

# *******
# Líneas en blanco
# *******

# Dos líneas en blanco para rodear clases y funciones

class A:
     pass


class B:
     pass


def funcion_a():
     pass


def funcion_b():
     pass

# Una línea en blanco para separar métodos dentro de una clase
class A:
     def __init__(self):
          pass
     
     def metodo_a(self):
          pass
     
# Una línea en blanco para separar secciones lógicas dentro de una función
# Más a la interpretación del programador (Usar con moderación)
def funcion_a(cantidad):
    if cantidad > 10:
        raise ValueError('La cantidad no puede se mayor a 10')
    else:
        cantidad += 1

    mi_cantidad = cantidad * 0.15 + 1000
    
    return mi_cantidad

# *******
# Codificación
# *******

# Utilizar UTF-8 en Python 3 Y ASCII en Python 2
# Se recomienda utilizar ASCII
# Se recomienda utilizar palabras en inglés como identificadores

# *******
# Acerca de los import Import
# *******

# Ubicados al comienzo del script, entre el docstring y las variables
# y constantes del módulo

# INTRODUCIR ENTRE CADA GRUPO UNA LÍNEA EN BLANCO

# Orden:
# 1. Librerías estándar.
# 2. Librerías de terceros.
# 3. Librerías locales.

# Import de varios módulos
import sys, os # MAL

import sys # BIEN
import os # BIEN

# Import de varios elementos de un mismo módulo
from random import randint, choice # BIEN

# Import absolutos cuando se trata de paquetes (en la medida de lo posible)
import paquete_personal.subpaquete.modulo as p # BIEN

# No se recomienda utilizar el asterisco
from random import * # MAL

# *******
# Uso de comillas
# *******

# Si utilizamos comillas simples, que sea siempre así.
# Si utilizamos comillas dobles, que sea siempre así.
# Evitar el uso de escapes para representar comillas

'''
Esto es muy "Pythónico" --> BIEN (PEP 8 RECOMIENDA ESTA FORMA)
Esto no es muy 'Pythónico' --> MAL
'''

# *******
# Espacios en blanco
# *******

# No usar en blanco: después de un paréntesis, corchete, llave.
# No usar en blanco: antes de una coma, punto y coma, dos puntos.

# MAL, espacio después de la llave de apertura y antes del cierre
# MAL, espacio antes de los dos puntos
diccionario = { 'clave' : 'valor' } 

# CORRECTO
diccionario = {'clave': 'valor'}

# SLICING SIN ESPACIOS
cadena = 'Hola Mundo'
cadena[0 : 5] # MAL
cadena[0:5] # BIEN

# No utilizar más de un espacio antes y después de los operadores
a = 10 + 20 # BIEN
a = 10       +     30 # MAL (no hace falta alinear las operaciones)
b = 10383822 + 324323 # BIEN

# Sobre operadores binarios y sus agrupaciones. 
# Se pueden agregar los espacios en blanco en los operadores de más baja prioridad.

x= 10 + 20 * 30 + 40 # MAL

calculo_total = 10 + 20*30 + 40 # BIEN

# En los valores por defecto de las funciones, no dejar espacios en blanco alrededor del =

def funcion_a(a, cantidad=10): # BIEN
    pass

def funcion_a(a, cantidad = 10): # MAL
    pass

# No poner esepacios entre el nombre de la función o método y los argumentos.
print ('hola mundo') # MAL

#********
# Trailing comas (comas finales).
#********

tupla = (1, 2, 3, ) # MAL (SOBRA EL ESPACIO FINAL)
tupla = (1, 2, 3,) # BIEN

#********
# Comentarios de bloque
#********

# Llevan un espacio en blanco entre el asterisco y el texto
# Escribir en inglés
# No más de 72 caracteres por línea
# Deben hacer referencial código que sigue a continuación

def calcular(cantidad):
    # Este algoritmo toma un valor
    # lo multiplica por 10
    # y lo imprime en un papel con
    # una impresora de tinta
    resultado = cantidad * 10
    print(resultado) # En papel (Esto es un comentario de una línea, separado por espacios del código)


#********
# Docstring (cadena de documentación)
#********

# Se utiliza para documentar módulos, clases, funciones y métodos
# Se utiliza comillas triples (triple comilla doble)
# Inmediatamente después del elemento que documentan
# El texto debe ser en inglés
# El texto va a continuación de las comillas triples sin espacio

def sumar(sumando_1, sumando_2):
    """
    This function takes two arguments
    and returns the sum of them.
    """
    return sumando_1 + sumando_2

class Calculadora:
    """
    This class represents a calculator
    that can add, subtract, multiply and divide.

    Attributes:
    nombre: A string representing the name of the calculator

    """
    def __init__(self, nombre):
        """
        The constructor of the class
        """
        self.nombre = nombre

calculadora = Calculadora('Calculadora de Python')
# print(help(Calculadora ))

#********
# Convenciones de nombres - nomenclatura
#********
nombre_de_variable = 10

def nombre_de_funcion():
    pass

class NombreClase:
    def nombre_metodo(self):
        pass

ESTO_ES_UNA_CONSTANTE = 10

# Módulos
# nombre_de_modulo.py
# nombredepaquete.subpaquete.nombre_de_modulo.py
# Variables de tipo: Num
# Excepciones --> Igual que las clases (en realidad son clases)

#********
# Recomendaciones de programación
#********

# Utilizar los operadores is o not is para comparar objetos (en lugar de == o !=)
cantidad = 10

if cantidad is not None: # BIEN
    pass

if cantidad != None: # MAL
    pass

# Utilizar los operadores is o not is en lugar de comparar con True o False utilizando == o !=
superior = cantidad > 1000

if superior is True: # BIEN
    pass

if superior == True: # MAL
    pass

# (MEJOR OPCIÓN) No Utilizar los operadores is o not is para comparar con True o False
superior = cantidad > 1000

if superior: # ¡MEJOR AÚN!
    pass

# No negar expresiones booleanas con if not
if not superior is None: # MAL
    pass

if superior is not None: # BIEN
    pass

#********
# Excepciones
#********

# No capturar solo utilizando except (Ejemplo siguiente)
try:
    10/0
except:
    print('Error')

#********
# Evaluación de prefijos y sufijos
# Utilizr starswith y endswith en lugar de slicing
#********
fichero = 'loquesea.txt'
if fichero[-4:] == '.txt': # MAL
    pass

if fichero.endswith('.txt'): # BIEN
    pass




    