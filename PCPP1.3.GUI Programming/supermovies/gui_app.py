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

class SuperMovieGUI:
    APP_TITLE = 'SuperMovie'
    VERSION = '1.0'
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry(f'{SuperMovieGUI.WINDOW_WIDTH}x{SuperMovieGUI.WINDOW_HEIGHT}')
        self.window.title = f'{SuperMovieGUI.APP_TITLE}. {SuperMovieGUI.VERSION}'

        self.__create_buttons_bar()
        self.__create_search_frame()

        self.window.mainloop()

    def __create_buttons_bar(self):
        #region Creación del Frame
        buttons_frame = tk.Frame(self.window, height=100, bg='#AAAAAA')
        buttons_frame.pack(fill='x', anchor='n')
        #endregion

        #region Creación de los botones (dentro del frame)
        self.b_search = tk.Button(buttons_frame, text='Buscar', height=2, command=self.__search_movie)
        self.b_search.grid(row=0, column=0)
        self.b_save = tk.Button(buttons_frame, text='Guardar', height=2, command=self.__save_movie)
        self.b_save.grid(row=0, column=1)
        #endregion

    def __create_search_frame(self):
        #region Creación del Frame
        # Ocupa todo el espacio disponible, gracias a fill y a expand
        self.search_frame = tk.Frame(self.window, bg='#EEEEEE')
        self.search_frame.pack(fill='both', expand=True)
        # endregion

        #region Creación del Formulario de búsqueda
        self.l_search_title = tk.Label(self.search_frame, text='Título a buscar:')
        self.l_search_title.place(x=200, y=50)

        self.e_search_title = tk.Entry(self.search_frame, width=50)
        self.e_search_title.place(x=300, y=50)

        self.l_title = tk.Label(self.search_frame, text='Título:')
        self.l_director = tk.Label(self.search_frame, text='Director:')
        self.l_plot = tk.Label(self.search_frame, text='Sinopsis:')
        self.l_year = tk.Label(self.search_frame, text='Año de estreno:')

        self.l_title.place(x=200, y=100)
        self.l_director.place(x=200, y=140)
        self.l_plot.place(x=200, y=180)
        self.l_year.place(x=200, y=360)

        self.e_title = tk.Entry(self.search_frame, width=50)
        self.e_director = tk.Entry(self.search_frame, width=50)
        self.t_plot = tk.Text(self.search_frame, height=10, width=40)
        self.sp_year = tk.Spinbox(self.search_frame, width=5, from_=1900, to=2025)

        self.e_title.place(x=300, y=100)
        self.e_director.place(x=300, y=140)
        self.t_plot.place(x=300, y=180)
        self.sp_year.place(x=300, y=360)

        #endregion

    def __search_movie(self):
        title = self.e_search_title.get().strip()
        if (title==''):
            self.__show_warning('Debe introducir un título para poder realizar una búsqueda')

    def __save_movie(self):
        title = self.e_title.get().strip()
        director = self.e_director.get().strip()
        #1.0 Es línea 1, primer carácter
        plot = self.t_plot.get('1.0', tk.END).strip() 
        year = int(self.sp_year.get())
        if (title==''):
            self.__show_warning('No hay datos para almacenar')
        else:
            print(title, director, plot, year)

    def __show_warning(self, text):
        messagebox.showwarning(SuperMovieGUI.APP_TITLE, text)

    