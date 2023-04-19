import tkinter as tk

window = tk.Tk() #generar ventana


#hay geometrias
#primero hay que crear witches
#crear una etiqueta
                        #en que ventana lo voy a situar  #text
label_saludo = tk.Label(window, text="Hola", bg="yellow", fg="blue")
label_saludo.pack(ipadx=30, ipady=30, side='left')


label_adios = tk.Label(window, text="Adios", bg="red", fg="white")
label_adios.pack(ipadx=30, ipady=30)

window.mainloop() #loop

