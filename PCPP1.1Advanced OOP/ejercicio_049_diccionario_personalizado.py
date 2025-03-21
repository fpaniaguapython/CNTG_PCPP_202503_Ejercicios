'''
Queremos disponer de un dict de tipos concretos en los que las claves
van a ser str y los valores van a ser instancias de la clase
Cliente
'''
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return f'Cliente:{self.nombre}'

class MiDiccionario(dict):
    __key_type = str
    __value_type = Cliente
    def __init__(self, *args, **kwargs):
        print('__init__')
        for k, v in kwargs.items():
            if (not isinstance(k, MiDiccionario.__key_type)):
                raise TypeError('La clave tiene que ser un entero')
            if (not isinstance(v, MiDiccionario.__value_type)):
                raise TypeError('El valor tiene ser un Cliente')
        super().__init__(*args, **kwargs)

    def __setitem__(self, key, value):
        if (not isinstance(key, MiDiccionario.__key_type)):
            raise TypeError('La clave tiene que ser un entero')
        if (not isinstance(value, MiDiccionario.__value_type)):
            raise TypeError('El valor tiene ser un Cliente') 
        return super().__setitem__(key, value)

mi_diccionario = MiDiccionario()
mi_diccionario = MiDiccionario(**{'cliente_1' : Cliente('Cliente 1'), 'cliente_2' : Cliente('Cliente 2')})
mi_diccionario = MiDiccionario(cliente_1 = Cliente('Cliente 1'), cliente_2 = Cliente('Cliente 2'))
# mi_diccionario = MiDiccionario(cliente_1 = Cliente('Cliente 1'), cliente_2 = 'Texto') # Error
print(mi_diccionario.get("cliente_2"))

mi_diccionario['cliente_3'] = Cliente('Cliente 3')
# mi_diccionario[4] = Cliente('Cliente 4') # TypeError: La clave tiene que ser un entero
# mi_diccionario['cliente_4'] = 'Cliente 4'# TypeError: El valor tiene ser un Cliente
