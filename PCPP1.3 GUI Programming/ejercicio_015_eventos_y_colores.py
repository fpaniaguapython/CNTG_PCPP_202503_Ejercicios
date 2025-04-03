'''
En una ventana vamos a poner tres Label con los textos ROJO, VERDE y AZUL en sus colores respectivos
Debajo hay un botón

Cuando se pasa el ratón por encima de alguno de los label se cambia el color de fondo del botón
al color correspondiente (y el texto en blanco)

Al salir de los Label se deja en su estado inicial.
'''
import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title('Ejemplo pack')
main_window.geometry('400x200')

def cambiar_color(color):
    boton['bg']=color

label_1 = tk.Label(main_window, text='Rojo', fg='red')
label_2 = tk.Label(main_window, text='Verde', fg ='#00FF00')
label_3 = tk.Label(main_window, text='Azul', fg='blue')
boton = tk.Button(main_window, text='Soy un botón')

color_inicial = boton['bg']

label_1.bind('<Enter>', lambda evento, color='red' : cambiar_color(color))
label_2.bind('<Enter>', lambda evento, color='green' : cambiar_color(color))
label_3.bind('<Enter>', lambda evento, color='blue' : cambiar_color(color))
label_1.bind('<Leave>', lambda evento, color=color_inicial : cambiar_color(color))
label_2.bind('<Leave>', lambda evento, color=color_inicial : cambiar_color(color))
label_3.bind('<Leave>', lambda evento, color=color_inicial : cambiar_color(color))

label_1.pack()
label_2.pack()
label_3.pack()
boton.pack()

main_window.mainloop()