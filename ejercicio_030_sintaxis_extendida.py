def calcular():
    print('Sin argumentos')

calcular()

def calcular(argumento):
    print('Con argumento', argumento)

calcular(20)    

def calcular(argumento = 10 ):
    print('Con argumento opcional', argumento)

calcular()
calcular(30)
calcular(argumento=40)

def calcular(argumento1, argumento2, *args):
    print(type(args)) # <class 'tuple'>
    print(args) # (5, 6)

calcular(3, 4, 5, 6)

def calcular(argumento1, argumento2, **kwargs):
    print(type(kwargs)) # <class 'dict'>
    print(kwargs) # {'salario': 3000, 'antiguedad': 4}

calcular(1, 2, salario=3_000, antiguedad=4)

# def calcular(**kwargs, *args): # Error
# def calcular(*args, argumento_keyword, **kwargs): # Ok (ver línea 37)
def calcular(*args, **kwargs): # Ok
    print(args)
    print(kwargs)

calcular(8, 9, salario=2_500, antiguedad=7)
# calcular(8, 9, argumento_posicional = 10, salario=2_500, antiguedad=7)

# REENVÍO DE LOS ARGUMENTOS A OTRA FUNCIÓN
def super_combiner(*my_args, **my_kwargs):
    print('my_args:', my_args)
    print('my_kwargs', my_kwargs)

def combiner(a, b, *args, **kwargs):
    super_combiner(*args, **kwargs) # Esta es la línea relevante

combiner(10, '20', 40, 60, 30, argument1=50, argument2='66')


# OBLIGAR A QUE LOS ARGUMENTOS SEAN POSIONALES O DE TIPO KEYWORD
# a, b, deben ser posicionales obligatoriamente
# c, d, pueden ser posicionales o keyword
# e, f, deben ser keyword obligatoriamente
def calcular(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

calcular(3, 3, 3, d=3, e=3, f=3)