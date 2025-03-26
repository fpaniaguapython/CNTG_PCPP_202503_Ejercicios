import tkinter as tk

main_window = tk.Tk()
main_window.title('Ejemplo pack')
main_window.geometry('800x600')

button = tk.Button(main_window, text='Boton')
label = tk.Label(main_window, text='Label')
entry = tk.Entry(main_window, width=20)

button.pack()
label.pack()
entry.pack()

# Crear un interfaz que solicite el título de una película
# Cuando se pulsa un botón:
# - valida si hay API-KEY
# - valida que hay algo en el widget entry
# Si no hay nada, utilizamos un messagebox de error.
# Si hay algo llamamos a un función que muestra el texto escrito

# Además se va a solicitar una API-KEY (clave de acceso) junto con un botón guardar.

main_window.mainloop()