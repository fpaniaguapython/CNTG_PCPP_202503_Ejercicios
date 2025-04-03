import traceback 

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
    print(traceback.format_tb(me.__traceback__))

'''
['  File "c:\\ejercicio_054_atributo_trackback.py", line 16, in <module>\n    resultado = dividir(8, 0)\n',
 '  File "c:\\ejercicio_054_atributo_trackback.py", line 11, in dividir\n    raise  MiException(\'Ha pasado algo\') from zde\n']
'''