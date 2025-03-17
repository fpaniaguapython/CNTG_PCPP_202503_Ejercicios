class MiException(Exception):
    pass

def dividir(n1, n2):
    try:
        resultado = n1 / n2
    except ZeroDivisionError as zde:
        # OJO AL from zde, ya que es lo que da info a __cause__
        raise  MiException('Ha pasado algo') from zde 
    return resultado


try:
    resultado = dividir(8, 0)
except MiException as me:
    print(me)
    print('__context__:', me.__context__) # division by zero
    print('__couse__:', me.__cause__) # division by zero
