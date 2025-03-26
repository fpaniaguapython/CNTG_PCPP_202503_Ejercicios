import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title('Ejemplo pack')
main_window.geometry('800x600')

# Solicitar una API-KEY (clave de acceso) junto con un botón guardar.
# Solicitar el título de una película, junto con un botón buscar.
# Cuando se pulsa un botón buscar:
# - valida si hay API-KEY
# - valida que hay algo en el widget entry
# Si no hay nada, utilizamos un messagebox de error.
# Si hay algo llamamos a un función que muestra el texto escrito

api_key = None

def save_api_key():
    global api_key
    api_key = entry_api_key.get()
    entry_api_key['state']=tk.DISABLED
    print(f'Guardando el API_KEY: {api_key}')

def search_movie():
    if (api_key is None):
        messagebox.showerror('Error', 'No has introducido el API_KEY')
    else:
        movie_title = entry_titulo.get()
        if (len(movie_title.strip())==0):
            messagebox.showerror('Error', 'No has introducido ningún título')
        else:
            print(f'Buscando {movie_title}')

# API_KEY

label_api_key = tk.Label(main_window, text='API KEY:')
entry_api_key = tk.Entry(main_window, width=20)
button_save_api_key = tk.Button(main_window, text='Guardar', command=save_api_key)

label_api_key.place(x=50, y=50)
entry_api_key.place(x=130, y=50)
button_save_api_key.place(x=270, y=47)

# PELICULA

label_titulo = tk.Label(main_window, text='Título:')
entry_titulo = tk.Entry(main_window, width=20)
button_search = tk.Button(main_window, text='Buscar', command=search_movie)

label_titulo.place(x=50, y=90)
entry_titulo.place(x=130, y=90)
button_search.place(x=270, y=87)

main_window.mainloop()