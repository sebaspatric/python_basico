def miFuncion(nombre):
    print("Hola mundo", nombre)
    
def suma(a, b):
    print(a + b)

def matematicas (a, b):
    def suma(a, b):
        print(a + b)
    def resta (a, b):
        print(a - b)
    suma(a, b)
    resta(a, b)



print("--------------")

suma(1, 2)

matematicas(5, 3)






if __name__ == '__main__':
    miFuncion("d")