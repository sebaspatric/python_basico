#map filter and reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

lista = ["pepe", "pepito", "juan"]

def miFuncion(x):
    condicion = str(x).startswith('pep')
    if condicion:
        return True
    
    return False

result1 = list(filter(miFuncion, lista))


result2 = list(filter(lambda x: str(x).startswith('pep'), lista))
print(result1)
print(result2)


