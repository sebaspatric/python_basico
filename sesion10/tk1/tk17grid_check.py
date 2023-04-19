import sys
import tkinter as tk
from tkinter import ttk

window = tk.Tk() #generar ventana


#funcion
def mifuncion():
    print(selected.get())

#grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

selected = tk.StringVar() #variable value

checkbox = ttk.Checkbutton(window, text="Checkbutton", variable=selected, command=mifuncion
                           )
checkbox.grid(row=0, column=0)



window.mainloop() #loop

sys.exit(0)

