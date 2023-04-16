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
    def __init__(self):
        print("Inicializando el dino")
    def verEscamas(self):
        pass

print("--------potato------------------")

#zona de memoria
#instancia1
p = Potato()
p.enciende()
print(p.isEncendido())
p.apaga()
print(p.isEncendido())

print("--------dino------------------")
d1 = Dino()
d1.apaga()
print(d1.isEncendido())

print("-------propiedades-------------------")

p= Dino()
print(dir(p))
print("--------------------------")

print("--------------------------")