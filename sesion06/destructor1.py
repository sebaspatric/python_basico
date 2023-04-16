print("--------herencia------------------")

#herencia

class Juguete:  #python2 class Juguete(object):
    _encendido = True
    
    def enciende(self):
        print("Enciende el aparato")
        self._encendido = True

    def apaga(self):
        print("Apaga el aparato")
        self._encendido = False #self modifica la variable global
    
    def isEncendido(self):
        return self._encendido
    

class Potato(Juguete):    
    def quitarOreja(self):
        pass
    def ponerOreja(self):
        pass

class Dino(Juguete):  
    color = None
    nombre = None

    def __init__(self, nombre):
        print("Inicializando el dino", nombre)
        self.nombre = nombre
        self.color = "blanco"

    def __del__(self): ## se invoca cuando no hay más referencias
        print("Estoy en el destructor del dino", self.__class__)
    
    def verEscamas(self):
        pass

print("--------dino------------------")
d1 = Dino("victoria")
print(d1.nombre)
print(d1.color)
d1.apaga()
print(d1.isEncendido())

print("-------propiedades-------------------")

p= Dino("victor")
print(dir(p))
print("--------------------------")

print("--------------------------")