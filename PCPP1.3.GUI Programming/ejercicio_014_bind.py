import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title('Ejemplo pack')
main_window.geometry('400x200')

def saludar(event):
    messagebox.showinfo('Saludador','¡Hola!')
    print(type(event)) # <class 'tkinter.Event'>
    print(event) # <ButtonPress event num=1 x=14 y=13>

label = tk.Label(main_window, text='Púlsame')
# Utilizamos la función bind
label.bind('<Button-1>', saludar) # Pulsar con el ratón
label.bind('<Enter>', lambda evento: print('Entrando')) # Mouse over
label.bind('<Leave>', lambda evento: print('Saliendo')) # Mouse leave
label.pack()


main_window.mainloop()