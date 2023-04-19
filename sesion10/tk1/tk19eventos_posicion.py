import tkinter as tk
from tkinter import Message, mainloop, ttk
#no funciona
#window = tk.Tk() #generar ventana

#funcion

def motion(event):
    print("Mouse position: (%s %s)", (event.x, event.y))
    return 


#evento

master = tk.Tk()
texto = "Demo de texto widget msg para ver el movimiento del ratón"
msg = Message(master, text=texto)
msg.config(bg='lightgreen', font=('time', 24, 'italic'))
msg.bind('<Motion>', motion)
msg.pack

mainloop()

#window.mainloop() #loop

#sys.exit(0) 


