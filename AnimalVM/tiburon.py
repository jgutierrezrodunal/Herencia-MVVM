from animal import Animal
from Observable import observable


class Tiburon(Animal):

    def __init__(self, especie, edad):
        self.especie = observable(especie)
        self.edad = observable(edad)

    def voz(self):
        print("glu glu glu")  

    def moverse(self):
        print("Nadando con aletas")