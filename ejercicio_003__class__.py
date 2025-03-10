class Factura:
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        pass

factura = Factura(1000)
print(Factura.__class__) # <class 'type'>
print(factura.__class__) # <class '__main__.Factura'>
print(factura.numero.__class__) # <class 'int'>
print(factura.calcular.__class__) # <class 'method'>