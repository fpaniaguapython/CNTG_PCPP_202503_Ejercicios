import tkinter as tk
import tkinter.messagebox as msgbox

main_window = tk.Tk()
main_window.title("GUI Película")
main_window.geometry("400x300")


def get_entry_text_api_key(entry):
    if entry.get().strip() == "":
        msgbox.showwarning("API-KEY WARNING",
                           "Es necesario introducir una API KEY",)
    else:
        print(f"Hay algo en el entry de la API KEY: {entry.get()}")


def get_entry_text_pelicula(entry_pelicula, entry_api_key):
    if entry_pelicula.get().strip() == "":
        msgbox.showwarning("PELÍCULA WARNING",
                           "Es necesario introducir una Película",)
    elif entry_api_key.get().strip() == "":
        msgbox.showwarning("API-KEY WARNING",
                           "Es necesario introducir una API KEY",)
    else:
        print(f"Hay algo en el entry de la película: {entry_pelicula.get()}")


label_pelicula = tk.Label(main_window, text="Película: ")
entry_pelicula = tk.Entry(main_window, width=20)
label_api_key = tk.Label(main_window, text="API-KEY: ")
entry_api_key = tk.Entry(main_window, width=20)
button_guardar = tk.Button(main_window, text="Guardar",
                           command=lambda entry=entry_api_key: get_entry_text_api_key(entry))
button_registrar = tk.Button(main_window, text="Registrar", command=lambda entry_pelicula=entry_pelicula,
                             entry_api_key=entry_api_key: get_entry_text_pelicula(entry_pelicula, entry_api_key))

label_pelicula.grid(row=0, column=0)
entry_pelicula.grid(row=0, column=1)
label_api_key.grid(row=1, column=0)
entry_api_key.grid(row=1, column=1)
button_guardar.grid(row=1, column=2)
button_registrar.grid(row=3, columnspan=3)

main_window.mainloop()
