class Mando:
    def siguiente_canal(self):
        raise NotImplementedError('No implementado')
    def canal_anterior(self):
        pass
    def subir_volumen(self):
        pass
    def bajar_volumen(self):
        pass

class MandoSony(Mando):
    pass

mando = Mando()
#mando.siguiente_canal()