from Observable import observable


class Animal:

    def __init__(self, especie, edad):
        self.edad = observable(edad)
        self.especie = observable(especie)


    def voz(self):
        pass

    def moverse(self):
        pass