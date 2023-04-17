import pprint

pprint.pprint(dir(''))

cadena = "en un lugar de la mancha"
print(cadena.lower().count('a'))

otracadena = cadena.lower().replace('e', ' ')
print(otracadena) 

numero = '5'
print(numero.isdigit())

numero = 'a2!'
print(numero.isdigit())
print(numero.isalpha())
print(numero.isalnum())

print(otracadena.strip())

print(cadena.split())

print(cadena.split('en'))

print(cadena.lower().endswith('mancha'))