# 1. Menú (todavía no)
# 2. (Frame 1) Barra de botones en un frame con un botón 'buscar' y un botón de 'guardar'.
# 3. (Frame 2) Label (Título de la película) y una caja de texto.
# 4. (Frame 2) Ficha de la película con Entrys para los siguientes campos:
# - Título
# - Director
# - Sinopsis
# - Año de estreno
# 5. Cuando se pulse el botón 'buscar' se comprobar que hay algo en la caja de texto.
# 6. Cuando se pulse el botón 'guardar' se comprueba que hay algo en la caja del título.

import tkinter as tk
from tkinter import messagebox

main_window = tk.Tk()
main_window.title("Supermovies")
main_window.geometry("456x456")


def check_title(entry):
    if entry.get().strip() == "":
        messagebox.showwarning("TÍTULO WARNING",
                               "Es necesario introducir un título",)
    else:
        print(f"Título introducido: {entry.get()}")


# menu_frame = tk.Frame(main_window, width=200, height=100, bg='#B8B8B8')
# menu_frame.grid(row=0, column=0)
label_fake = tk.Label(
    main_window, text="Archivo  |  Editar  |  Acerca de...  |")
label_fake.grid(row=0, column=0, sticky="w")


# Frame
aux_frame = tk.Frame(main_window, width=456, height=100, bg='#AAAAAA')
aux_frame.grid(row=1, column=0, columnspan=2)

button_search = tk.Button(main_window, text="Buscar")
button_save = tk.Button(main_window, text="Guardar")
button_search.grid(row=1, column=0, sticky="w")
button_save.grid(row=1, column=1, sticky="w")

# Frame
main_frame = tk.Frame(main_window, width=456, height=400, bg='#B8B8B8')
main_frame.grid(row=2, column=0, columnspan=2, rowspan=10)

label_title_search = tk.Label(main_window, text="Título a buscar: ")
entry_title_search = tk.Entry(main_window, width=30)
label_title_search.grid(row=2, column=0, sticky="w")
entry_title_search.grid(row=2, column=1, sticky="w")

label_movie_title = tk.Label(main_window, text="Título: ")
entry_movie_title = tk.Entry(main_window, width=30)
label_movie_title.grid(row=5, column=0, sticky="w")
entry_movie_title.grid(row=5, column=1, sticky="w")

label_movie_director = tk.Label(main_window, text="Director: ")
entry_movie_director = tk.Entry(main_window, width=30)
label_movie_director.grid(row=6, column=0, sticky="w")
entry_movie_director.grid(row=6, column=1, sticky="w")

label_movie_synopsis = tk.Label(main_window, text="Sinopsis: ")
entry_movie_synopsis = tk.Entry(main_window, width=30)
label_movie_synopsis.grid(row=7, column=0, sticky="w")
entry_movie_synopsis.grid(row=7, column=1, sticky="w")

label_release_year = tk.Label(main_window, text="Año de estreno: ")
entry_release_year = tk.Entry(main_window, width=30)
label_release_year.grid(row=8, column=0, sticky="w")
entry_release_year.grid(row=8, column=1, sticky="w")

button_search.configure(
    command=lambda entry=entry_title_search: check_title(entry))
button_save.configure(
    command=lambda entry=entry_title_search: check_title(entry))

main_window.mainloop()
