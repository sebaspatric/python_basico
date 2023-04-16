
#funcion anonima
print("--------------------")

anonima = lambda: print("hola mundo")
anonima()

anonima = lambda nombre, nombre2: print("hola", nombre, "adios", nombre2)
anonima("mundo", "mundo2")


print("--------------------")


anonima = lambda a,b: a+b

print(anonima(3,4))
