import tkinter as tk

"""
En una ventana vamos a poner tres Label con los textos ROJO, VERDE y AZUL, en sus colores respectivos.
Cuando se pasa el ratón por encima de alguno de los Labels, se cambia el color de fondo del Label al color correspondiente
y el texto en blanco.

Al salir del Label, vuelve a su estado inicial.
"""

ENTER = '<Enter>'
LEAVE = '<Leave>'

COLOR_RED = 'red'
COLOR_GREEN = 'green'
COLOR_BLUE = 'blue'
COLOR_WHITE = 'white'


main_window = tk.Tk() 
main_window.title('Ejemplo bind')
main_window.geometry('400x300')

def change_color(event, bg_color):   
    event.widget.config(bg=bg_color, fg=COLOR_WHITE)

def reset_color(event):   
    event.widget.config(bg=main_window.cget('bg'), fg=event.widget.original_fg)

label_red = tk.Label(main_window, text='ROJO', fg=COLOR_RED, padx=10, pady=5)
label_green = tk.Label(main_window, text='VERDE', fg=COLOR_GREEN, padx=10, pady=5)
label_blue = tk.Label(main_window, text='AZUL', fg=COLOR_BLUE, padx=10, pady=5)

label_red.original_fg = COLOR_RED
label_green.original_fg = COLOR_GREEN
label_blue.original_fg = COLOR_BLUE

label_red.bind(ENTER, lambda event: change_color(event, COLOR_RED))
label_red.bind(LEAVE, reset_color)

label_green.bind(ENTER, lambda event: change_color(event, COLOR_GREEN))
label_green.bind(LEAVE, reset_color)

label_blue.bind(ENTER, lambda event: change_color(event, COLOR_BLUE))
label_blue.bind(LEAVE, reset_color)

label_red.grid(column=0, row=0, padx=20, pady=10)
label_green.grid(column=0, row=1, padx=20, pady=10)
label_blue.grid(column=0, row=2, padx=20, pady=10)

main_window.mainloop()
