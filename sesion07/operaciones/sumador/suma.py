class Sumatorio:

    def suma(self, a, b):
        """
        Suma dos números
        :param a:
        :param b:
        :return:
        """
        return a + b

    def add(self, a, b):
        return a + b


#no vamos a tener código de ámbito global en los módulos
#sólo funciones clases y variables
print("Hola, estoy en suma y soy  el módulo: ", __name__)