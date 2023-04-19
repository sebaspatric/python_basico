import tkinter as tk
from tkinter import Message, mainloop, ttk
from tkinter import filedialog
from tkinter import colorchooser

window = tk.Tk()
            #ventana para abrir ficheros
filename = filedialog.askopenfilename()

colorchooser.askcolor(initialcolor="#ff0000")
window.mainloop()

#window.mainloop() #loop

#sys.exit(0) 


