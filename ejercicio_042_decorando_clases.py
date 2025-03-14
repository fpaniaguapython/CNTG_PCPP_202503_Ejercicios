def funcion_generar_pdf(self):
    print(f'Generando pdf para la factura {self.numero}')
    self.generado = True

def decorador(clase_a_decorar):
    # ************************
    # En este punto, disponemos de una referencia a la clase
    # Podemos añadir métodos y atributos de clase
    # ************************
    print('Definición del decorador (solo una vez)')
    clase_a_decorar.generar_pdf = funcion_generar_pdf
    print(clase_a_decorar.__dict__)
    # ************************
    # Fin de añadir métodos y atributos de clase
    # ************************
    def inner_wrapper(*args, **kwargs):
        print('inner_wrapper - args:', args)
        print('inner_wrapper - kwargs:', kwargs)
        instancia = clase_a_decorar(*args, **kwargs)
        # *****************************************************************
        # En este punto, disponemos de una referencia al objeto (instancia)
        instancia.generado = False
        # *****************************************************************
        return instancia
    return inner_wrapper

@decorador
class Factura:
    def __init__(self, numero, importe):
        self.numero = numero
        self.importe = importe

    def get_numero(self):
        return self.numero
    
factura_1 = Factura(101, 15_000)
numero_factura = factura_1.get_numero()
print(numero_factura)
factura_1.generar_pdf()
print('Factura 1 (generado):', factura_1.generado)

factura_2 = Factura(102, 25_000)
factura_2.generar_pdf()
print('Factura 2 (generado):', factura_2.generado)

factura_3 = Factura(103, 80_000)
print('Factura 3 (generado):', factura_3.generado)