def get_saludo(nombre : str) -> str:
    # return 10 # No da error
    return f'Hola {nombre}'


get_saludo(100) # No da error
get_saludo(True) # No da error
get_saludo([1,2,3]) # No da error
get_saludo('Rodrigo')