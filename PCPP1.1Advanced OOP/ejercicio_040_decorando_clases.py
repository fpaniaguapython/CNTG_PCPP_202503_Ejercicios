def validador(clase_a_decorar):
    # Obteniendo una referencia al método de obtención de valores de atributos
    clase_a_decorar.atributos = clase_a_decorar.__getattribute__
    
    def validar(self, nombre_atributo):
        if nombre_atributo=='importe':
            if clase_a_decorar.atributos(self, nombre_atributo) > 1000:
                raise ValueError('No se pueden leer las cantidades mayores de 1000')
        return clase_a_decorar.atributos(self, nombre_atributo)
    
    # Redefiniendo el comportamiento del método de obtención de valores de atributos
    clase_a_decorar.__getattribute__ = validar
    return clase_a_decorar

@validador
class Factura:
    def __init__(self, numero, importe):
        self.numero = numero
        self.importe = importe

factura_1 = Factura('001',1_000)

print(factura_1.numero) # Ok, no lo valida
print(factura_1.importe) # Ok, lo valida y cumple con la condicion
factura_1.importe = 2_000
#print(factura_1.importe) # KO. Genera un ValueError
