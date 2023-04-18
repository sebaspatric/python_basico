#reduce ejecuta de forma recursiva una funcion sobre la lista hasta que se quede con un único elemento

from functools import reduce


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

lista = ["pepe", "pepito", "juan"]

def suma(x, y):
    print(f'a={x}, y={y}')
    return x + y

res1 = reduce(suma, numeros)
res2 = reduce(lambda x, y: x + y, numeros)
res3 = reduce(lambda x, y: x + y, lista)

print(res1)
print(res2)
print(res3)


'''
contar el número de palabras de un diccionario

a=1, y=2
a=3, y=3
a=6, y=4
a=10, y=5
a=15, y=6
a=21, y=7
a=28, y=8
a=36, y=9
a=45, y=10
a=55, y=11
66

'''
