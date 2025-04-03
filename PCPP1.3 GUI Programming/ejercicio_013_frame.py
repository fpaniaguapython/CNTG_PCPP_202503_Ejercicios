import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Ventana
main_window = tk.Tk()
main_window.title('Ejemplo pack')
main_window.geometry('400x200')

# Frame
frame = tk.Frame(main_window, width=200, height=100, bg='#AAAAAA')
frame.pack(fill='x', anchor='n')

# Botón (dentro del frame)
button_1 = tk.Button(frame, text='Pulsa', height=2)
button_1.grid(row=0, column=1)
button_2 = tk.Button(frame, text='Pulsa', height=2)
button_2.grid(row=0, column=2)

main_window.mainloop()