import tkinter as tk
from tkinter import ttk

window = tk.Tk() #generar ventana

#play posisionamiento

label1 = tk.Label(window, text="Posicionamiento absoluto1", bg = "blue", fg = "white")
label1.place(x = 10, y = 50)


label2 = tk.Label(window, text="relativo", bg = "red", fg = "yellow")
#label2.place(relx=0.10, rely=0.15, relwidth=0.5, anchor='ne')
label2.place(x=25, y=30)



window.mainloop() #loop

