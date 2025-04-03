# Versión de José Luis

import tkinter as tk

main_window = tk.Tk()
main_window.title('3 En Raya')
main_window.geometry('150x150')

turno = ['X']  

def switch(button):
    if button['text'] == '':  
        button.config(text=turno[0])
        turno[0] = "O" if turno[0] == 'X' else 'X' 

botones = []

for filas_indice in range(3):  
    fila = []
    for columnas_indice in range(3):  
        boton = tk.Button(main_window, text='', width=5, height=2)
        boton.config(command=lambda b=boton: switch(b))  
        boton.grid(row=filas_indice, column=columnas_indice)
        fila.append(boton)
    botones.append(fila)

main_window.mainloop()
