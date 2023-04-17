def suma(a, b):
    return a + b

class Multiplicador:
    def multiplica(self, a, b):
        return a * b


#no vamos a tener código de ámbito global en los módulos
#sólo funciones clases y variables
print("Hola, estoy en suma y soy  el módulo: ", __name__)