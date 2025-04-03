import tkinter as tk
from tkinter import messagebox

botones = []
fichas = ['O','X']
turno = 0

def seleccionar_celda(boton_pulsado):
    global turno
    if (boton_pulsado['text'] == ''):
        turno+=1
        boton_pulsado['text']=fichas[turno%2]

def reiniciar_tablero():
    respuesta = messagebox.askokcancel('Reinicio', '¿Quiere reiniciar')
    if respuesta:
        for boton in botones:
            boton['text']=''

tablero = tk.Tk()
tablero.title('3 EN RAYA')
tablero.geometry('450x540')

for fila in range(3):
    for columna in range(3):
        boton = tk.Button(
            tablero, 
            text='', 
            width=20, 
            height=10)
        boton['command']=lambda boton_pulsado=boton : seleccionar_celda(boton_pulsado)
        boton.grid(row=fila, column=columna)
        botones.append(boton)

boton_reset = tk.Button(tablero, 
                        text='Reiniciar partida', 
                        width=63, height=3,
                        command=reiniciar_tablero)
boton_reset.grid(row=3, column=0, columnspan=3)




tablero.mainloop()
