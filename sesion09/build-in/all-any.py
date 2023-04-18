listaA = [1 == 1, 2 == 2, 3 == 3, 4 == 4, 5 == 5, 6 == 7]

res = all(listaA) ##verificar  a que todas sean ciertas
print(res)

res2 = any(listaA) ##verificar  a que algunas sean ciertos
print(res2)


#round

a = 1.5
b = 2.5
c = 3.5

print(round(a))
print(round(b))
print(round(c))

#min
print(min(a,b,c))

#pow
print(pow(a,b))

print('---------------------------')
#ordenar
lista = [1,2,3,9,5,6,7,8,9]
print(sorted(lista))
print(sorted(lista,reverse=True))
print(sorted(lista,key=lambda x:x))
ordenada = sorted(lista,key=lambda x:x,reverse=True)
print(ordenada)
lista = ['a','b','C','d','e']
ordenada = sorted(lista,key=lambda x:str(x).startswith('d'), reverse=True)
print(ordenada)