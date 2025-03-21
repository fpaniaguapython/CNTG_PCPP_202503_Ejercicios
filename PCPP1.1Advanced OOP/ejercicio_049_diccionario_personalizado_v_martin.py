class Cliente:
    def __init__(self, nombre: str, apellidos: str, dni: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni

    def __repr__(self):
        return f"Cliente(Nombre: {self.nombre}, Apellidos: {self.apellidos}, DNI: {self.dni})"
    
class DictTipado(dict):
    key_type = str
    value_type = str

    @classmethod
    def validate_items(self, clients: dict):
        return all(self.validate_item(k,v) for k, v in clients.items())
    
    @classmethod
    def validate_item(self, k: int, v: Cliente):
        if not isinstance(k, self.key_type) :
            raise TypeError('Clave incorrecta')
        
        if not isinstance(v, self.value_type):
            raise TypeError('Tipo Cliente incorrecto')

    def __init__(self, initial: dict = {}):
        self.validate_items(initial)
        super().__init__(initial)

    def __setitem__(self, key, value):
        self.validate_item(key, value)
        return super().__setitem__(key, value)

class ListaClientes(DictTipado):
    key_type = int
    value_type = Cliente