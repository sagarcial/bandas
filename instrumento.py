class Instrumento:
    def __init__(self, nombre, puede_afinar=False):
        self.nombre = nombre
        self.puede_afinar = puede_afinar

    def afinar(self):
        if self.puede_afinar:
            print(f"Afinando {self.nombre}")
        else:
            print(f"{self.nombre} no se puede afinar")
    def tocar(self):
        pass
    def consultar(self):
        print("Soy: ", self.nombre)

class Piano(Instrumento):
    def __init__(self):
        super().__init__("Piano")

class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("Guitarra")

class Saxofon(Instrumento):
    def __init__(self):
        super().__init__("Saxofon")

class Bajo(Instrumento):
    def __init__(self):
        super().__init__("Bajo")

if __name__ == "__main__":
    a = Piano()
    a.consultar()