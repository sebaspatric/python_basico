
##named parametros
def sumar(a,b):
    return a + b

def operacion(a,b):
    return a + b, a - b, a * b, a / b, a ** b
        
result = sumar(1,2)
print(result)
print("---------------------")

result = operacion(1,2)
print(result)
print(result[1])
print("---------------------")

suma, resta, multiplicacion, division, potencia = operacion(1,2)

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(potencia)
print("---------------------")

res = operacion(1,2)
print(res[1])

_, restas, _, _, _ =operacion(1,2)

print(restas)

if __name__ == '__main__':
    sumar("d",'j')