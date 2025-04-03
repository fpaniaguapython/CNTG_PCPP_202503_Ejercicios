# VER TRANSPARENCIAS Y CURSO. TEORÍA SOBRE EL MODELO DE COLOR RGB

import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title('Ejemplo pack')
main_window.geometry('400x200')

# bg -- background 
# fg -- foreground
# activebackground
# activeforeground

button_save_api_key = tk.Button(main_window, text='Guardar',
                                width=10, height=10,
                                bg='red', fg='white',
                                activebackground='beige', activeforeground='red')
button_save_api_key.pack()

main_window.mainloop()
