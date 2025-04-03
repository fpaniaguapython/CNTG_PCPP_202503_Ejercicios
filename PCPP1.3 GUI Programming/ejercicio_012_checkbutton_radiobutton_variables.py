import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title('Ejemplo pack')
main_window.geometry('400x200')

def mostrar():
    print(intercambio.get()) # Obtenemos el valor de la variable intercambio

# Declaración de la variable compartida 'intercambio'
# Existen IntVar, DoubleVar, BooleanVar, StringVar
intercambio = tk.BooleanVar() # Declaración
intercambio.set(True) # Asignación

checkbutton_1 = tk.Checkbutton(main_window, text='Seleccionar 1', variable=intercambio)
checkbutton_2 = tk.Checkbutton(main_window, text='Seleccionar 2')

radiobutton_1 = tk.Radiobutton(main_window, text='Opción 1', value=True, variable=intercambio)
radiobutton_2 = tk.Radiobutton(main_window, text='Opción 2', value=False, variable=intercambio)

button = tk.Button(main_window, text='Pulsa', command=mostrar)

checkbutton_1.pack()
checkbutton_2.pack()
radiobutton_1.pack()
radiobutton_2.pack()
button.pack()


main_window.mainloop()