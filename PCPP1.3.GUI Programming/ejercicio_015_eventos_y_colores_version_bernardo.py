import tkinter as tk

main_window = tk.Tk()
main_window.title('Ejemplo')
main_window.geometry('200x200')

def establecer_color(label, color):
    label.config(bg=color, fg='white')

def eliminar_color(label):
    label.config(bg=main_window.cget("bg"), fg='black')

def pintar(label):
    label.pack(anchor='center', expand=True)

def detectar_entrada(label, color):
    label.bind('<Enter>', lambda x: establecer_color(label, color))

def detectar_salida(label):
    label.bind('<Leave>', lambda x: eliminar_color(label))


label_rojo = tk.Label(main_window, text='ROJO')
label_verde = tk.Label(main_window, text='VERDE')
label_azul = tk.Label(main_window, text='AZUL')

pintar(label_rojo)
pintar(label_verde)
pintar(label_azul)

detectar_entrada(label_rojo, 'red')
detectar_entrada(label_verde, 'green')
detectar_entrada(label_azul, 'blue')

detectar_salida(label_rojo)
detectar_salida(label_verde)
detectar_salida(label_azul)

main_window.mainloop()
