# Clase Cliente que tenga 3 atributos.

# Clase ClienteVIP que herede de Cliente y tenga 2 atributos más.

# En la clase ClienteVIP tendrá un método saludar. Muestra un mensaje.

# En la clase ClienteVIP tendrá un método modificar que va a crear
# un atributo llamado saludar.

# Desde fuera, crear una instancia de ClienteVIP
# e invocar CON SEGURIDAD al método saludar.

class Cliente:
    def __init__(self, nombre, sexo, ganancias):
        self.nombre = nombre
        self.sexo = sexo
        self.ganancias = ganancias


class ClienteVIP(Cliente):
    def __init__(self, nombre, sexo, ganancias, titulo, descuento):
        super().__init__(nombre, sexo, ganancias)
        self.titulo = titulo
        self.descuento = descuento


    def saludar(self):
        print(f"Hola, me llamo {self.nombre}")


    def modificar(self):
        #setattr(self, "saludar", f"Hola, me llamo {self.nombre}")
        self.saludar = 'Hola'


cliente = ClienteVIP("Juan", "M", 1000, "VIP", 0.1)

# cliente.modificar() # Con esta línea, el atributo no es ejecutable

if hasattr(cliente, "saludar"):
    if callable(cliente.saludar):
        cliente.saludar()
    else:
        print("Tengo de eso, pero no es ejecutable")
else:
    print("No tengo de eso")