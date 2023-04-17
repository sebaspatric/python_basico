f = open('/etc/passwd', 'r')
"""
"""
datos = None

while datos != "":
    datos = f.readline()
    print(datos)

f.close()
print("-------------")
print(datos)

