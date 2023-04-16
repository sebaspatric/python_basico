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
    def __init__(self, nombre):
        print("Inicializando el dino", nombre)
    def verEscamas(self):
        pass

print("--------dino------------------")
d1 = Dino("victoria")
d1.apaga()
print(d1.isEncendido())

print("-------propiedades-------------------")

p= Dino("victor")
print(dir(p))
print("--------------------------")

print("--------------------------")