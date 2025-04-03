import tkinter as tk
def blink():
    global is_white
    if is_white:
        color = 'black'
    else:
        color = 'white'
    is_white = not is_white
    frame.config(bg=color)
    frame.after(500, blink) # Invoca a la función transcurridos 500ms
is_white = True
window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='white')
frame.after(500, blink) # Invoca a la función transcurridos 500ms
frame.pack()
window.mainloop()