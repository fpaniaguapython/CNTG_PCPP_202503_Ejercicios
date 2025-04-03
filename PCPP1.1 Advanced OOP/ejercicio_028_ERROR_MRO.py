# Method Resolution Order
class A:
    def info(self):
        print('A')

class B(A):
    def info(self):
        print('B')

class C(A):
    def info(self):
        print('C')

# class D(B, A): # No hay problema, toma la versión de B
class D(A, B): # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, B
    pass