'''
Tcl/Tk

libreríá tkinter usa tk
'''
from tkinter import *

class Alumno:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title('hola mundo')
if __name__ == '__main__':
    ventana = Tk()
    alumno = Alumno(ventana)
    ventana.mainloop()
    