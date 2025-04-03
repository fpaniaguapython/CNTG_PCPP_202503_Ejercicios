import abc # Módulo referente a las clases abstractas

class Motor(abc.ABC):
    def __init__(self, nombre):
        self.nombre=nombre

    def arrancar(self):
        print('Arrando el motor', self.nombre)

    @abc.abstractmethod
    def acelerar(self):
        pass

class MotorCombustion(Motor):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def acelerar(self):
        print('Soy el motor', self.nombre, 'y estoy acelerando')

# motor_v8 = Motor('V8') # Esta instanciación no es posible

motor_v8 = MotorCombustion('V8') # Solo va a ser posible si MotorCombustion implementa el método acelerar
