#map funcion a todos los elementos de un elemento iterable... lista



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

lista = ["pepe", "pepito", "juan"]

def cuadrado(x):
    return x * x

result1 = map(cuadrado, numeros)

result2 = list(map(lambda x: x * x, numeros))

print(list(result1))

print(result2)