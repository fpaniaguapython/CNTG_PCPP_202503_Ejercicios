# Method Resolution Order
class A:
    def info(self):
        print('A')

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.info() 
# D, si está en D; 
# B, si no está en D y está en B
# C, si no está en D ni en B pero está en C 
# A, si no está en D, C, B, pero está en A