temperatura = 12.0


def miFuncion(nombre="juan"):
    hoyHace = 6.0
    print("la t° es ", temperatura)
    print("Hola mundo", nombre,"la t° es ", hoyHace)

miFuncion()
miFuncion("victor")

def suma(a, b=5, c=1):
    print(a + b+c)
suma(3)
suma(1,1,1)
suma(1, c=9)
suma(b=1, a=3, c=9)


if __name__ == '__main__':
    miFuncion("d")