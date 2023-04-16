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


print("--------------------------")

#modelo de datos
class Usuario:
    Nombre = ""
    Apellido = ""
    

