import sys
import tkinter as tk
from tkinter import ttk

window = tk.Tk() #generar ventana

#funcion

def saludo(event):
    print("Hola mundo")

def saludarDobleclick(event):
    print('han hecho doble click en saludar')
    #rint(event.widget.cget("text"))
    #rint(event.widget.winfo_x(), event.widget.winfo_y())
    #rint(event.widget.winfo_width(), event.widget.winfo_height())
    #rint(event.widget.winfo_rootx(), event.widget.winfo_rooty())

def salir(event):
    print("Hasta luego")
    window.quit()

#evento

boton = tk.Button(window, text="Boton")
boton.pack() #mostrarlo
#banding unir un evento a una acción
boton.bind("<Button-1>", saludo) 
boton.bind("<Double-1>", saludarDobleclick)

boton2 = tk.Button(window, text="Boton2")
boton2.pack() #mostrarlo
boton2.bind("<Button-2>", lambda event: print(event.widget.cget("text")))
boton2.bind("<Double-2>", lambda event: print(event.widget.cget("text")))

botonSalir = tk.Button(window, text="BotonSalir")
botonSalir.pack() #mostrarlo
#banding unir un evento a una acción
botonSalir.bind("<Button-1>", salir) 
botonSalir.bind("<Double-1>", saludarDobleclick)


window.mainloop() #loop

sys.exit(0) 


