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

variable = 5
print(variable)

globals()['variable'] = 6
print(variable)

def prueba():
    globals()['variable'] = 7

prueba()
print(variable)

if __name__ == "__main__":
    main()
