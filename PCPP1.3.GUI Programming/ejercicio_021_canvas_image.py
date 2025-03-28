import tkinter as tk

class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def mover(canvas : tk.Canvas, posicion : Posicion):
    posicion.x+=1
    canvas.create_image(posicion.x, 200, image=image)

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')
image = tk.PhotoImage(file='f1.png')
button = tk.Button(window, text="Quit",command=window.destroy)
posicion = Posicion(10, 200)
button_mover = tk.Button(window, text="Mover",
    command = lambda canvas_parametro=canvas, posicion_parametro=posicion : 
        mover(canvas_parametro, posicion_parametro))

canvas.grid(row=0)
button.grid(row=1)
button_mover.grid(row=2)
window.mainloop()