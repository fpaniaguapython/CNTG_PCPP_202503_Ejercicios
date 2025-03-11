class Motor:
    '''
    Soy un motor de combustión
    '''
    def __init__(self, nombre):
        '''
        Inicializador del motor
        '''
        self.nombre = nombre
    
    def arrancar(self):
        '''
        Arranca el motor
        '''
        pass

motor = Motor('V8')

print(help(Motor)) 

