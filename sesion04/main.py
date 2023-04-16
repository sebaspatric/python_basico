a = 5
b = 6
#> 
resultado = a<b
resultado = a>=b

resultado = (a>=5 & b<=6)

print(resultado)


#&
print("t & t", True & True)
print("t & f", True & False)
print("f & t", False & True)
print("f & f", False & False)

#o
print("t or t", True | True)
print("t or f", True | False)
print("f or t", False | True)
print("f or f", False | False)


#xor
print("t xor t", True ^ True)
print("t xor f", True ^ False)
print("f xor t", False ^ True)
print("f xor f", False ^ False)


a = 5
b = 6
c = 7
#> 
resultado = (a>=5 | c>7)& (b==5)

print(resultado)