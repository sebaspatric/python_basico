print("-----------------")
import math
import pprint

import operaciones.sumador as op
import operaciones.sumador.suma as s


def main():
    #codigo
    pprint.pprint(dir(op))
    print("----------------------")
    pprint.pprint(dir(s))
    print("----------------------")
    mivar = "a"
    pprint.pprint(dir(mivar))
    print("----------------------")
    tuple = (1,2,3)
    pprint.pprint(dir(tuple))
    print("----------------------")
    pprint.pprint(dir(math))
    ##math.floor()

    print("----------------------")
    obj = s.Sumatorio()
    obj.suma(2, 2)
    #obj.suma(1,2)

    help(obj.suma)


 

    

print("-----------------")
print("estoy en modulo4 y Soy el módulo", __name__)


if __name__ == "__main__":
    main()
