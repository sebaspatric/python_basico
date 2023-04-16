#composicion
#una clase tiene una o más instancias de otra

class Motor:
    tipo = "Diesel"

class Ventanas:
    cantidad = 5
    def cambiarCantidad(self, cantidad):
        self.cantidad = cantidad

class Ruedas:
    cantidad = 4


class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()


class Coche:
    motor = Motor()
    carroceria = Carroceria()

c = Coche()
print("motor es ", c.motor.tipo)
print("carroceria ventanas es ", c.carroceria.ventanas.cantidad)

c.carroceria.ventanas.cambiarCantidad(2)
print("carroceria ventanas es ", c.carroceria.ventanas.cantidad)