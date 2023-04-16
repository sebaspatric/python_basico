
#parametros variables
temperatura = 12.0


def miFuncion(nombre="juan"):
    hoyHace = 6.0
    print("la t° es ", temperatura)
    print("Hola mundo", nombre,"la t° es ", hoyHace)

print("---------------------")
def suma(*args):
    print(args)

suma(1,2,3,4,5)


print("---------------------")
def suma(*args):
    resultado = 0
    for i in args:
        resultado += i
    print(resultado)

suma(1,2,3,4,5)

print("------------------diccionario---")
def suma(**kwargs):
    print(kwargs)

suma(vivienda="piso", coche= "rojo")

print("------------------diccionario---")
def suma(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

suma(vivienda="piso", coche= "rojo")
print("------------------diccionario---")


##named parametros
def suma(**kwargs):
    if kwargs['coche'] == "bonito":
        print("bonito")
        
suma(coche="bonito")
print("------------------diccionario---")

##named parametros
def suma(**kwargs):
    if 'coche' in kwargs:
        if kwargs['coche'] == "bonito":
            print("bonito")
        
suma()
print("------------------diccionario---")





if __name__ == '__main__':
    miFuncion("d")