import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title('Ejemplo pack')
main_window.geometry('400x200')

def desvincular(event):
    label.unbind('<Button-1>') # Desvinculamos el evento
    label['text']='Ya no'
    messagebox.showinfo('Ejemplo','Botón desvinculado')
    
    

label = tk.Label(main_window, text='Púlsame')
label.bind('<Button-1>', desvincular) # Pulsar con el ratón
label.pack()


main_window.mainloop()