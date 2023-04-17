numeros = 511
texto = "Quijote"
otromas = 1.2

print("El numero es %d y el texto es %s y tiene %f"%(numeros, texto, otromas))
print("El numero flotante es %.2f "% otromas)

mensaje = ("El numero es {} y el texto es {} y tiene {}"
           .format(numeros, texto, otromas))
print(mensaje)
print("El numero es {1} y el texto es {0} y tiene {2}".format(texto, numeros, otromas))

print("El numero es {n1} y el texto es {t1} y tiene {d1}".format(t1=texto, n1=numeros, d1=otromas))


#hasta la python3.6

#referencia a las variables no hay  qque hacer transformaciones
print(f'El numero es {numeros} y el texto es {texto} y tiene {otromas}')

print(f'El numero es {numeros} y el texto es {texto.upper()} y tiene {otromas}')

def suma(a,b):
    return a+b

print(f'El numero es {suma(numeros, numeros)} y el texto es {texto.upper()} y tiene {otromas}')

txt = f'El numero es {suma(numeros,numeros)} y el texto es {texto.upper()} y tiene {otromas}'
print(txt)

num = 544
print(type(num))
numTxt = str(num)
print(type(numTxt))

print(repr(num))
print(numTxt)
