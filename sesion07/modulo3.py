print("-----------------")
from operaciones.sumador import suma as s
from operaciones.restador import resta as r
from operaciones import sumador as s1, restador as s1
#import operaciones.suma as suma
import pprint
import sys
print("-----------------")
pprint.pprint(sys.path)
print("-----------------")    
sys.path.append("../")#ruta que deseo agregar 


def main():
    #codigo
    sum = s.suma(4,2)
    res = r.resta(4,2)


    print("Hola mundo, suma =" , sum)
    print("Hola mundo, resta =", res)
 

    
    



print("-----------------")
print("estoy en modulo2 y Soy el módulo", __name__)


if __name__ == "__main__":
    main()
