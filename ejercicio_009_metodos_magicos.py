class Producto(object):
    def __init__(self, nombre, precio, referencia):
        self.nombre = nombre
        self.precio = precio
        self.referencia = referencia

    def __len__(self): # Es el método utilizado por la función len
        return self.precio
    
    def __str__(self): # Es el método utilizado por la función print
        return f"Producto: {self.nombre}, Precio: {self.precio}, Referencia: {self.referencia}"
    
    def __repr__(self):
        return f"Producto({self.nombre}, {self.precio}, {self.referencia})"

pendrive = Producto("Pendrive", 10, "A123")
cd = Producto("CD", 2, "B456")

print(len(pendrive)) # 10 --> Función len
print(pendrive) # Producto: Pendrive, Precio: 10, Referencia: A123 --> Utiliza __str__

productos = (pendrive, cd) # tuple
print(productos) # (Producto(Pendrive, 10, A123), Producto(CD, 2, B456)) --> Utiliza __repr__
