import tkinter as tk
from tkinter import ttk

window = tk.Tk() #generar ventana

#grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


#window.grid_columnconfigure(0, weight=1)
#window.grid_rowconfigure(0, weight=1)

#username---------------------------------------------------------------------
#label
username_label = ttk.Label(window, text="username:")
username_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5) #fijar ventana a la rejilla
# W west

#inputbox
username_entry = ttk.Entry(window)#, width=20)
username_entry.grid(row=0, column=1, sticky=tk.E, padx=5, pady=5) #fijar ventana a la rejilla

#password------------------------------------------------------------------------
#label
password_label = ttk.Label(window, text="password:")
password_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5) #fijar ventana a la rejilla
# W west

#inputbox
password_entry = ttk.Entry(window, show='*')#, width=20)
password_entry.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5) #fijar ventana a la rejilla

# Boton1-------------------------------------------------------------------------
login_button = ttk.Button(window, text="Login")#, command=login)
login_button.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5) #fijar ventana a la rejilla 

# Boton2-------------------------------------------------------------------------
login_button = ttk.Button(window, text="Login")#, command=login)
login_button.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5) #fijar ventana a la rejilla 


window.mainloop() #loop

