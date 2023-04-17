import pprint as pp

f = open('/etc/passwd', 'r')
"""
"""
datos = 'a'
datos = f.readlines()
f.close()
print("-------------")
pp.pprint(datos)

