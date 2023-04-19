import sys
import tkinter as tk
from tkinter import ttk

window = tk.Tk() #generar ventana

#grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

frame = ttk.Frame(window)


label = ttk.Label(frame, text="Hola mundo")
label.grid(row=0, column=0, sticky=tk.W, padx=50, pady=50)
frame.grid(row=1, column=0, sticky=tk.W, padx=50, pady=50) #frame no se ve pero sirve para posicionar objetos


window.mainloop() #loop

sys.exit(0)

