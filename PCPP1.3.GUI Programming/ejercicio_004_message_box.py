import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title(string='Mi APP TkInter')
main_window.geometry(newGeometry='400x300')

def show_info():
    messagebox.showinfo(title='Título', message='Mensaje')

def ask_question():
    respuesta = messagebox.askquestion(title='Título', message='Mensaje')
    print(respuesta)

boton_show_info = tk.Button(main_window, 
                          text='messagebox.showinfo', command=show_info)
boton_ask_question = tk.Button(main_window, 
                          text='messagebox.askquestion', command=ask_question)

boton_show_info.pack()
boton_ask_question.pack()

main_window.mainloop()