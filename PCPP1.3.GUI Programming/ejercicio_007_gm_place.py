import tkinter as tk

main_window = tk.Tk()
main_window.title('Ejemplo place')
main_window.geometry('800x600')

boton = tk.Button(main_window, text='Calcular')

boton.place(x=100, y=50, width=300, height=300) # Ancho y alto en píxeles

main_window.mainloop()