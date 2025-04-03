import tkinter as tk
import abc

class F1:
    def __init__(self, image_file, x, y, speed):
        self.image = tk.PhotoImage(file=image_file)
        self.x = x
        self.y = y
        self.speed = speed

    def mover(self, canvas : tk.Canvas):
        self.x+=self.speed
        canvas.delete('all')
        canvas.create_image(self.x, self.y, image=self.image)

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')

f1 = F1(image_file='f1.png', x=10, y=200, speed=2)
f1.mover(canvas=canvas)

window.bind_all('z', lambda event, canvas_parametro=canvas, f1_parametro=f1 : 
        f1_parametro.mover(canvas_parametro))

canvas.grid(row=0)
window.mainloop()