"""
Esta es la definición del módulo.
Para qué sirve, qué elementos contiene,
etc.
"""

def calcular(numero : int, instancia : int) -> int:
    """
    Esta función calcula el producto del númer
    y la instancia en un espacio interestelar
    superior.
    """    
    return numero * instancia

class Calculadora:
    """
    Representa una calculadora binaria
    """
    def __init__(self):
        """
        Constructor
        """
        pass
    def sumar(self, sumando_1 : int, sumando_2 : int) -> int:
        """
        Convierte a binario los sumandos y devuelve
        el resultado de su suma (en binario)
        """
        pass

    @staticmethod
    def __convertir_a_binario(numero : int) -> None:
        """
        Convierte un número a binario
        """
        # No hace falta documentar con docstring
        pass

    @staticmethod
    def __validar_numero(numero : int) -> None:
        Calculadora.__convertir_a_binario(numero)

calculadora = Calculadora()
calculadora.sumar(10, 20)
