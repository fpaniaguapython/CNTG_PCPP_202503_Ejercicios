import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title('Ejemplo pack')
main_window.geometry('400x200')

def saludar(event):
    print('Ha pulsado:', event)
    try:
        print(event.widget.unidades) # Leemos el atributo propio
    except:
        pass
    finally:
        messagebox.showinfo('Ejemplo','Hola')

label_1 = tk.Label(main_window, text='Label 1')
label_1.unidades = 10 # Agregamos un atributo propio
label_1.pack()
label_2 = tk.Label(main_window, text='Label 2')
label_2.unidades = 20 # Agregamos un atributo propio
label_2.pack()
label_3 = tk.Label(main_window, text='Label 3')
label_3.unidades = 30 # Agregamos un atributo propio
label_3.pack()

main_window.bind_all('<Button-1>', saludar)

main_window.mainloop()