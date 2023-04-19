import tkinter as tk

window = tk.Tk() #generar ventana


#hay geometrias
#primero hay que crear witches
#crear una etiqueta
                        #en que ventana lo voy a situar  #text
label1 = tk.Label(window, text="label1", bg="yellow", fg="blue")
label1.pack(ipadx=45, ipady=15, fill='x')

label2 = tk.Label(window, text="label2", bg="purple", fg="white")
label2.pack(ipadx=45, ipady=15, fill='x')

label3 = tk.Label(window, text="label3", bg="blue", fg="white")
label3.pack(ipadx=45, ipady=15, fill='x')

label4 = tk.Label(window, text="label4", bg="red", fg="blue")
label4.pack(ipadx=15, ipady=15, side='left')

label5 = tk.Label(window, text="label5", bg="yellow", fg="black")
label5.pack(ipadx=15, ipady=15, side='left')

label6 = tk.Label(window, text="label6", bg="red", fg="white")
label6.pack(ipadx=15, ipady=15, side='right')

window.mainloop() #loop

