from AnimalVM import animal
from AnimalVM import gato

class DatosView:
    def __init__(self, animalVM: animal):
        self.animalVM = animalVM
        self.animalVM.edad.suscribe(self.cambiar_edad)
        
    def cambiar_edad(self, nueva_edad):
        print(f"La edad ha sido cambiada a  {nueva_edad}")

    def mostrar_datos(self):
        print("Datos del animal:")
        print(f"Nombre: {self.animalVM.especie}")
        print(f"Edad: {self.animalVM.edad}")

def main():

    a1 = gato("egipcio", 5)
    vista = DatosView(a1)

    vista.mostrar_datos()

if __name__ == "__main__":
    main()