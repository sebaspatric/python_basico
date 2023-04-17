print("-----------------")
import math
import pprint

import operaciones.sumador as op
import operaciones.sumador.suma as s

def main():
    #codigo

    print("----------------------")
    obj = s.Sumatorio()
    obj.suma(2, 2)
    #obj.suma(1,2)

    pprint.pprint(globals())


print("-----------------")
print("estoy en ambitos y Soy el módulo", __name__)
print("-----------------")
class Hola:
    lero = False

    def otraFuncion(self):
        print("adios")
    def patata():
        print("toma")

h = Hola()
#invocar a un metodo a traves de global
globals()['Hola'].patata()


if __name__ == "__main__":
    main()
