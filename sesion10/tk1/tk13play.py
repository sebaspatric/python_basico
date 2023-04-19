import random
import tkinter as tk
from tkinter import ttk

window = tk.Tk() #generar ventana

#play posisionamiento

#colores

colors = ["red", "blue", "green", "yellow", "orange", "purple"]
for x in range(len(colors)):
    color = random.randint(0, len(colors)-1)
    color2 = random.randint(0, len(colors)-1)
    ancho = random.randint(0, 50)
    alto = random.randint(0, 100)
    label = tk.Label(window, text=colors[color], bg = colors[color], fg = colors[color2])
    #label.place(x = 10, y = 100+x*10)
    label.place(x=random.randint(0, 100), y=random.randint(0, 100), width=ancho, height=alto)


window.mainloop() #loop

