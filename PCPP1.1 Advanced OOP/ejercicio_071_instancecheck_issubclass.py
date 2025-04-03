class Televisor(type):
    def __instancecheck__(self, instance):
        print('Comprobando instancia...')
        pass

    def __subclasscheck__(self, subclass):
        print('Comprobando clase...')
        pass


class TelevisorOLED(metaclass=Televisor):
    pass

televisor = TelevisorOLED()
isinstance(televisor, TelevisorOLED)
