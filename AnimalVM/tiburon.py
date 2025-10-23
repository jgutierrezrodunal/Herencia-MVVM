from animal import Animal


class Tiburon(Animal):

    def __init__(self, especie, edad):
        super().__init__(especie, edad)

    def voz(self):
        print("glu glu glu")  

    def moverse(self):
        print("Nadando con aletas")