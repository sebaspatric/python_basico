import tkinter as tk

window = tk.Tk() #generar ventana


#hay geometrias
#primero hay que crear witches
#crear una etiqueta
                        #en que ventana lo voy a situar  #text
label_saludo = tk.Label(window, text="Hola", bg="yellow", fg="blue")
label_saludo.pack(fill='both')

label_adios = tk.Label(window, text="Adios", bg="red", fg="white")
label_adios.pack(fill='both')

window.mainloop() #loop

