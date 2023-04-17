print("-----------------")
from operaciones import suma
#import operaciones.suma as suma
import pprint
import sys
print("-----------------")
pprint.pprint(sys.path)
print("-----------------")    
sys.path.append("../")#ruta que deseo agregar 


def main():
    #codigo
    sum = suma.suma(1,2)

    print("Hola mundo, suma =" , sum)
    
    #paquete operaciones - modulo suma - clase multiplicador
    mp = suma.Multiplicador()
    print("Hola mundo, multiplicacion =", mp.multiplica(2,3))

    
    



print("-----------------")
print("estoy en modulo2 y Soy el módulo", __name__)


if __name__ == "__main__":
    main()
