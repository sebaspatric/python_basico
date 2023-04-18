import python_basico.sesion07.operaciones1 as op
import pprint
import sys
print("-----------------")
pprint.pprint(sys.path)
print("-----------------")    
sys.path.append("../")#ruta que deseo agregar 


def main():
    #codigo
    sum = op.suma(1,2)

    print("Hola mundo, suma" , sum)

    print(op.como_me_llamo())
    print("-----------------")
    print(sys.path)
    print("-----------------")
    print(sys.version)
    print("-----------------")
    pprint.pprint(sys.path)
    print("-----------------")
    
    

    print("-----------------")
    
    print(op.PI)
    print("-----------------")
    for i in range(1, 10):
        c = op.fibonacci(i)
        print(i, c)



print("-----------------")
print("Soy el módulo", __name__)


if __name__ == "__main__":
    main()
