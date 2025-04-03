class FormularioException(Exception):
    def __init__(self, *args, nombre_campo, valor_campo):
        super().__init__(*args)
        self.nombre_campo = nombre_campo
        self.valor_campo = valor_campo

    def notificar(self):
        print(f'Enviar un email al administrador: {self.nombre_campo}:{self.valor_campo}')

def rellenar_formulario(nombre : str, edad : int):
    if (not isinstance(nombre, str)):
        raise FormularioException('Error en el nombre', nombre_campo=nombre, valor_campo=edad)
    if (edad<18):
        raise FormularioException('Error en la edad', nombre_campo=nombre, valor_campo=edad)

try:
    rellenar_formulario('Fernando', 17)
except FormularioException as fe:
    print(fe.nombre_campo)
    print(fe.valor_campo)
    fe.notificar()