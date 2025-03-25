import tkinter as tk
import tkinter.messagebox as msgbox  # Mensaje emergente

main_window = tk.Tk()  # Crear la main window
main_window.title('Mi APP TkInter')
main_window.geometry('800x600')

def salir():
    respuesta = msgbox.askquestion('Salir', '¿Estás seguro de salir?')
    if respuesta == 'yes':
        main_window.destroy()  # Finaliza la aplicación
    else:
        print(respuesta)


boton_saludar = tk.Button(main_window, 
                          text='Saluda',
                          command=lambda: msgbox.showinfo('Saludo', 'Hola Mundo'))

# boton_saludar.pack() # Ubica el componente en el centro horizontal y arriba
# Ubica el componente en la posición (400, 300)
boton_saludar.place(x=400, y=300)

boton_salir = tk.Button(main_window, text='Salir', command=salir)
boton_salir.place(x=10, y=300)

main_window.mainloop()
