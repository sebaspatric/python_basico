print("-----------------")
import math
import pprint

import operaciones.sumador as op
import operaciones.sumador.suma as s

def main():
    #codigo

    pass


print("-----------------")
print("estoy en ambitos y Soy el módulo", __name__)
print("-----------------")

def suma(a, b):
    return a+b
def resta(a, b):
    return a-b
#pprint.pprint(globals())

def prueba(inicial):
    valor = 5
    estado = False
    def abc():
        pass
    pprint.pprint(locals())

prueba(2)


if __name__ == "__main__":
    main()
