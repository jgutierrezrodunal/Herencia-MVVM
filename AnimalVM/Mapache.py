from animal import Animal
from Observable import observable


class Mapache(Animal):

    def __init__(self, especie, edad):
        self.especie = observable(especie)
        self.edad = observable(edad)
    
    def voz(self):
        print("ggrrrr")  

    def moverse(self):
        print("Caminando a 4 patas")