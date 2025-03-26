import tkinter as tk

main_window = tk.Tk()
main_window.title('Ejemplo pack')
main_window.geometry('800x600')


boton_1 = tk.Button(main_window, text='Botón 1')
boton_2 = tk.Button(main_window, text='Botón 2')
boton_3 = tk.Button(main_window, text='Botón 3')
boton_4 = tk.Button(main_window, text='Botón 4', height=5)

boton_1.pack()
boton_2.pack()
boton_3.pack()
# side --> Ubica el componente en un lugar concreto (TOP, BOTTOM, LEFT, RIGHT)
# fill --> Expande el componente
boton_4.pack(side=tk.BOTTOM, fill=tk.X) # Usar expand=True para fill=tk.Y

main_window.mainloop()