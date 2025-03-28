import tkinter as tk

def observable_get(*args):
    print('Hemos leído el valor de la variable')

def observable_set(vid, ix, act):
    print('vid:',vid) # Identificador de la variable
    print('ix:', ix) # Índice o cadena vacía
    print('act:', act) # Acción
    print('Hemos asignado un valor a la variable')

window = tk.Tk()

# Una declaración explícita de una variables 'observable'
variable = tk.StringVar()
# El valor se asigna con set
variable.set('Texto inicial') 

# Hacemos que este botón lea el valor de la variable
boton_1 = tk.Button(window, text='Leer', command=lambda: variable.get())
boton_1.pack()

# Hacemos que este botón modifique el valor de la varialbe
boton_2 = tk.Button(window, text='Modificar', command=lambda: variable.set('Texto cambiado'))
boton_2.pack()

# Label
# El atributo textvariable utiliza el valor de la variable 'observable'
label = tk.Label(window, textvariable=variable)
label.pack()

# Entry
# El atributo textvariable utiliza el valor de la variable 'observable'
entry = tk.Entry(window, textvariable=variable)
entry.pack()

# Asignar el observador a la variable *** VINCULAMOS CAMBIOS EN LA VARIABLE CON FUNCIONES ***
r_obsid = variable.trace_add('read', observable_get) 
w_obsid = variable.trace_add('write', observable_set)

window.mainloop()