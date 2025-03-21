try:
    numero = 8 / 0
except ArithmeticError as ae:
    print(ae) # division by zero
    print(ae.args) # ('division by zero',)
    # print(ae.name) # Error. No existe el atributo.
    # print(ae.path) # Error. No existe

try:
    import modulo_inexistente
except ImportError as ie:
    print(ie) # No module named 'modulo_inexistente'
    print(ie.args) # ("No module named 'modulo_inexistente'",)
    print(ie.name) # modulo_inexistente
    print(ie.path) # None