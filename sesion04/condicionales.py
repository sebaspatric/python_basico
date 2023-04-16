a= 5
b=6
c=7

print(a==5)

condicion = a==5 & b<=6
print(condicion)

condicion = (a==5) & b<=6
print(condicion)

if False:
    print("jjj")
elif a==5:
    print("kkk")

contador = 0
while contador<=10:
    if contador%2 == 0:
        print(contador,"es par  ") 
    print(contador)
    contador += 1           

contador = 0
while contador<=10:
    if contador==5:
        print(contador,"rompe bucle  ")
        break
        print(contador,"es par  ") 
    print(contador)
    print("estoy aquí porque el contador es",contador," y no se ejecuta break ")
    contador += 1  
    

contador = 0
while contador<=10:
    contador +=1    
    if contador%2 == 0:
        print(contador,"es par  ") 
        continue
    print("estoy aquí porque el contador es",contador," y no se ejecuta continue ")
         
print("------------------------------")


lista = ['a',2,4,5,6,7,8,9]
for vaorActual in lista:
    print("valor actual", vaorActual)
print("------------------------------")

longitud = len(lista)
print("la lista tiene", longitud, "items")
print("------------------------------")

for numero in range(longitud):
    print(numero, lista[numero])
print("------------------------------")

for numero in range(1,11):
    print(numero)
print("------------------------------")


lista = ["hola", "mundo", "adios"]
for palabra in lista:
    print("palabra actual: ",palabra)
    if palabra == "mundo":
        print("he encontrado la palabra", palabra)
        break

print("------------------------------")

lista = [1, 2, 6, 4, 9, 6, 7, 8, 5]
print(lista)

print("------------------------------")

listaOrdenada = sorted(lista)
print(listaOrdenada)
print("------------------------------")

print("------------------------------")

print("------------------------------")


valor = 3
try:
    match valor:
        case 1:
            print("valor 1")
        case 2:
            print("valor 2")
        case 3:
            print("valor 3")    
        case 4:
            print("valor 4")
except:
    print("valor no encontrado")


print("------------------------------")

lista = ["hola", "mensaje", "adios"]
encontrado = False
for palabra in lista:
    if palabra == "mensaje":
        encontrado = True
        print("encontrado", palabra)
        break
if encontrado:
    print("encontrado")
else:
    print("no encontrado")



print("------------------------------")     

lista = ["hola", "", "adios"]
#encontrado = False
for palabra in lista:
    if palabra == "mensaje":
        print("encontrado")
        #encontrado = True
        break
##if encontrado:
##    print("encontrado")
else:
    print("no encontrado")


print("------------------------------")  