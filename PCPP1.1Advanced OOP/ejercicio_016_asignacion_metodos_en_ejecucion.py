class Calculadora:
    pass
c = Calculadora()

def restar(self, operando1, operando2):
    return operando1 - operando2

Calculadora.sumar = lambda self, operando1, operando2: operando1 + operando2
Calculadora.restar = restar

print(c.sumar(5, 10)) # 15
print(c.restar(5, 10)) # -5