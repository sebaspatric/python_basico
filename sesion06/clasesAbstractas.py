from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

    def diHola(self):
        print("Hola")

class Perro(Animal):
    #debo implementar el metodo como tiene un metodo abstracto
    def sonido(self):
        print("Guau")

class Gato(Animal):
    def sonido(self):
        print("Miau")


p = Perro()
p.sonido()
p.diHola()

g = Gato()
g.sonido()
g.diHola()