def main():
    #codigo
    print("Hola mundo")

def como_me_llamo():
    return __name__

PI = 3.1415926535897932

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):  
    return a/b

def modulo(a,b):
    return a%b

def factorial(a):
    return a*factorial(a-1)

def potencia(a,b):
    return a**b
def raiz(a):    
    return a**(1/2)

def primo (a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True 

def cuadradobinomio(a,b,c):
    return (a**2+b**2+c**2)**(1/2)

def triangulo(a,b,c):
    return (a**2+b**2-c**2)**(1/2)

def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    





if __name__ == "__main__":
    main()
