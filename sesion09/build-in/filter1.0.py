#map filter and reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def miFuncion(x):
    if x % 2 == 0:
        return True
    
    return False

result1 = list(filter(miFuncion, numeros))

result2 = list(filter(lambda x: x % 2 == 0, numeros))
print(result1)
print(result2)


