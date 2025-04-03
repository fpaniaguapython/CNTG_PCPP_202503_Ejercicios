import tkinter as tk
import tkinter.messagebox as msgbox  # Mensaje emergente
from tkinter import ttk

main_window = tk.Tk()  # Crear la main window
main_window.title('Mi APP TkInter')
main_window.geometry('400x300')

boton_tk = tk.Button(main_window, 
                          text='Botón tk')

boton_ttk = ttk.Button(main_window, 
                          text='Botón ttk')

boton_tk.pack()
boton_ttk.pack()

main_window.mainloop()
