f = open('/etc/passwd', 'r')
"""
"""
datos = 'a'

while len(datos) > 0:
    datos = f.readline()
    print(datos)

f.close()
print("-------------")
print(datos)

