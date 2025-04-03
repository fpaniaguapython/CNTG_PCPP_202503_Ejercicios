import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title(string='Mi APP TkInter')
main_window.geometry(newGeometry='400x300')

boton_1 = tk.Button(main_window, 
                          text=' ',
                          width=5,
                          height=5)
boton_2 = tk.Button(main_window, 
                          text=' ')
boton_3 = tk.Button(main_window, 
                          text=' ')

boton_1.grid(row=0, column=0)
boton_2.grid(row=0, column=2)
boton_3.grid(row=1, column=1)

# Modificar el contenido de un widget
boton_3['text']='Hola'


main_window.mainloop()