class Dino:
    _encendido = True
    
    def enciende(self):
        self._encendido = True

    def apaga(self):
        self._encendido = False #self modifica la variable global
    
    def isEncendido(self):
        return self._encendido
    
#zona de memoria
#instancia1
d1 = Dino()
d1.apaga()
print(d1.isEncendido())

#zona de memoria
#instancia2
d2 = Dino()
d2.enciende()
print(d2.isEncendido())

print("--------------------------")

#clase estatica coparte un mismo lugar en memoria
#las variables internas se van a manipular
class Estatica:
    numero = 1

    def incrementa():
        Estatica.numero += 1

Estatica.incrementa()
print(Estatica.numero)
Estatica.incrementa()
print(Estatica.numero)
Estatica.incrementa()
print(Estatica.numero)


