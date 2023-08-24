from tkinter import *
from intertest import *
from intertest2 import *


root=Tk()
barra_Menu=Menu(root)
root.config(menu=barra_Menu, width=300, height=300)


def resultado_up():
    llamada2=StringVar()
    llamada2.set(boton_start2)
    
    
    
def resultado_down():
    llamada=StringVar()
    llamada.set(boton_start)
    
   


miFrame=Frame(root)
miFrame.pack()

label_uno=Label(miFrame, text="Speed Download: ")
label_uno.grid(row=1, column=0, sticky="e", padx=10)

label_dos=Label(miFrame, text="Speed Upload: ")
label_dos.grid(row=2, column=0, sticky="e", padx=10)

label_tres=Label(miFrame, text=" Mb/s", padx=10)
label_tres.grid(row=1, column=3)

label_cuatro=Label(miFrame, text=" Mb/s", padx=10)
label_cuatro.grid(row=2, column=3)

boton_start=Button(miFrame, text="Start", command=server_bajada())
boton_start.grid(row=1, column=1, sticky="e", padx=10, pady=10)
boton_start.config(justify="right")

boton_start2=Button(miFrame, text="Start", command=server_subida())
boton_start2.grid(row=2, column=1, sticky="e", padx=10, pady=10)
boton_start2.config(justify="right")

cuadro_uno=Entry(miFrame, textvariable=server_bajada())
cuadro_uno.grid(row=1, column=2, padx=10, pady=10)


cuadro_dos=Entry(miFrame, textvariable=server_subida())
cuadro_dos.grid(row=2, column=2, padx=10, pady=10)



root.mainloop()