class Pelicula:
    def __init__(self, titulo, numero_entradas, precio_entrada):
        self.titulo =  titulo
        self.numero_entradas = numero_entradas
        self.precio_entrada = precio_entrada
        self.__recaudacion = self.numero_entradas * self.precio_entrada

    def cotillear_recaudacion(self, other):
        # Se puede acceder a atributos 'privados' de otros de la misma clase
        print('Cotilleando:',other.__recaudacion) 

    @property # Es el getter del atributo
    def recaudacion(self):
        return self.__recaudacion
    
    @recaudacion.setter # Es el setter del atributo
    def recaudacion(self, nueva_recaudacion):
        self.__recaudacion = nueva_recaudacion

    @recaudacion.deleter # La encapsulación de un delattr
    def recaudacion(self):
        raise Exception('No se puede eleminar el atributo recaudación')
        

    '''
    # Forma tradicional

    # getter
    def get_recaudacion(self):
        return self.__recaudacion
    
    # setter
    def set_recaudacion(self, nueva_recaudacion):
        self.__recaudacion = nueva_recaudacion'
    '''

if __name__=='__main__':
    pelicula_01 = Pelicula('El resplandor', 100, 15)
    print(pelicula_01.titulo) # El resplandor
    # print(pelicula.__recaudacion) # Error
    print(pelicula_01._Pelicula__recaudacion) # 1500 (aunque no lo debemos utilizar)

    pelicula_02 = Pelicula('Tiburón', 80, 2000)
    pelicula_02.cotillear_recaudacion(pelicula_01)

    # print(pelicula_01.get_recaudacion()) # Para que funcione, hay que descomentar la función get_recaudacion
    print(pelicula_01.recaudacion) #1500
    pelicula_01.recaudacion=2_000
    print(pelicula_01.recaudacion) #2000

    try:
        delattr(pelicula_01, 'recaudacion') # Debe generar una excepción
    except Exception as e:
        print(e)