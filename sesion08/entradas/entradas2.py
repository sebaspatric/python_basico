class Juguete:
    nombre = ""
    precio = 0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    #sobrecargar el metodo con str
    #representaciones informales de texto
    def __str__(self):
        #return "Nombre: " + self.nombre + " Precio: " + str(self.precio)
        return f"Nombre: {self.nombre}, Precio: {self.precio}"
    
    #sobrecarga a repre
    #para codigos de depuracion
    #si tenemos rpr pero no str se ejecuta rpr
    def __repr__(self):
        return f"Juguete({self.nombre},{self.precio})"



j1 = Juguete("Juguete1", 10.5)
print(j1)

demo1 = j1
print(type(demo1))
demo1 = str(j1) #representaccion textual
print(type(demo1))

print(repr(j1))