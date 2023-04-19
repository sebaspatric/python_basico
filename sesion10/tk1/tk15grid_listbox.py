import sys
import tkinter as tk
from tkinter import ttk

window = tk.Tk() #generar ventana

#grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

lista = ['Windows', 'Linux', 'MacOS', 'MS DOS', 'Android', 'AmigaOS', 'BeOS', 'OS/2', 'Solaris', 'SunOS', 'FreeBSD', 'NetBSD']
lista_items = tk.StringVar(value=lista)

listbox = tk.Listbox(window, height=30, width=30, listvariable=lista_items)
listbox.grid(row=0, column=0, sticky=tk.W)#, padx =50, pady=50)


window.mainloop() #loop

sys.exit(0)

