
##named parametros
def sumar(a,b):
    return a + b

def sumador(**kwargs):
    inicial = kwargs['a']
    final = kwargs['b']

    resultado = 0
    for i in range(inicial,final+1):
        resultado += i
    return resultado

print(sumador(a=1,b=2))

print("--------------------")

def sumador(**kwargs):
    inicial = kwargs['a'] if 'a' in kwargs else 0
    final = kwargs['b'] if 'b' in kwargs else inicial
    # final = kwargs['b'] ? kwargs['b'] = 0

    resultado = 0
    for i in range(inicial,final+1):
        resultado += i
    return resultado

print(sumador())
print(sumador(a=3))
print(sumador(b=15))
print(sumador(b=5))



if __name__ == '__main__':
    sumar("d",'j')