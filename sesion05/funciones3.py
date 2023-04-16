
    
temperatura = 12.0


def miFuncion(nombre):
    hoyHace = 6.0
    print("la t° es ", temperatura)
    print("Hola mundo", nombre,"la t° es ", hoyHace)

miFuncion("victor")

def miFuncion2(nombre):
    temperatura = 6.0
    print("la t° es ", temperatura)
    print("Hola mundo", nombre,"la t° es ", temperatura)

miFuncion2("victor")
print(temperatura)


def miFuncion3(nombre):
    global temperatura ##afecta a la variable global
    temperatura = 6.0
    print("la t° es ", temperatura)
    print("Hola mundo", nombre,"la t° es ", temperatura)

miFuncion3("victor")
print(temperatura)



if __name__ == '__main__':
    miFuncion("d")