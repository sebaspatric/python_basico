print("--------herencia------------------")

#herencia

class Juguete:  #python2 class Juguete(object):
    _encendido = True

    #constructor
    def __init__(self, x):
        print("Inicializando el juguete", x)
        
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

    #constructor
    def __init__(self, nombre):
        super().__init__(nombre)
        print("Inicializando el dino", nombre)
        self.nombre = nombre
        self.color = "blanco"

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