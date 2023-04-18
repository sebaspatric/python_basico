secret = 50

valor = int(input("Digite um valor: "))


if valor % 2 == 0:
    print("O valor {} é par.".format(valor))
else:
    print("O valor {} é impar.".format(valor))

while valor != secret:
    valor = int(input("Digite um valor: "))
    if valor > secret:
        print("muy alto")
        continue
    if valor < secret:
        print("menor muy bajo")
        continue
print("Acabou")
