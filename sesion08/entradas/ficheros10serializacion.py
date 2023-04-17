"""
guargar datos en un fichero y luego recuperarlos
"""
import pickle
class Juguete:
    nombre = ""
    precio = 0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return "Nombre: " + self.nombre + " Precio: " + str(self.precio)
    
    def getNombre(self):
        return self.nombre
    
##instancia de juguete ...
j1 = Juguete("Juan", 100)

print(type(j1))

print(j1.getNombre())
print("----------------------------------------------------------")
#serializacion en fichero
fichero = "juguete2.bin"
f = open(fichero, "wb") #datos binarios
pickle.dump(j1, f) #lo que voy a serializar y donde...
f.close()

print("----------------------------------------------------------")
#deserializacion en fichero
f = open(fichero, "rb")
j2 = pickle.load(f)
f.close()

print(j2.getNombre())
print(j2.precio)
