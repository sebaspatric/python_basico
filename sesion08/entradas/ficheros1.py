f = open('/etc/passwd', 'r')
"""
r = f.read()
a = append
w = escritura
x = create
t = texto
b = binary
+
"""
"""
datos = f.read(28) #cuenta los saltos de linea como 1 caracter \n
f.close()

print(datos)

"""
datos = f.read(28) #cuenta los saltos de linea como 1 caracter \n
#f.close()

print(datos)


datos2 = f.readline() #cuenta los saltos de linea como 1 caracter \n
f.close()

print(datos2)