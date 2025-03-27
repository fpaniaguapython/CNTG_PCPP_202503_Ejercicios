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
    WINDOW_MIN_WIDTH = 640
    WINDOW_MIN_HEIGHT = 480
    WINDOW_MAX_WIDTH = 1024
    WINDOW_MAX_HEIGHT = 768
    ICON = 'icon.png'
    def __init__(self):
        self.__create_window()
        self.__create_menu()
        self.__create_buttons_bar()
        self.__create_search_frame()

        self.window.mainloop()

    def __create_window(self):
        self.window = tk.Tk()
        
        # Título
        self.window.title(f'{SuperMovieGUI.APP_TITLE}. {SuperMovieGUI.VERSION}')
        
        # Icono
        icon = tk.PhotoImage(file=SuperMovieGUI.ICON) # Crear un objeto con la imagen
        self.window.iconphoto(True, icon)
        
        # Tamaño
        self.window.geometry(f'{SuperMovieGUI.WINDOW_WIDTH}x{SuperMovieGUI.WINDOW_HEIGHT}')
        # Restricción de tamaño mínimo
        #self.window.minsize(width=SuperMovieGUI.WINDOW_MIN_WIDTH, height=SuperMovieGUI.WINDOW_MIN_HEIGHT)
        # Restricción de tamaño máximo
        #self.window.maxsize(width=SuperMovieGUI.WINDOW_MAX_WIDTH, height=SuperMovieGUI.WINDOW_MAX_HEIGHT)
        # Restricción de cambio de tamaño
        self.window.resizable(width=False, height=False)

        # Protocol
        # Intercepta el cierre de la ventana (no el fin de la aplicación)
        self.window.protocol('WM_DELETE_WINDOW', self.__do_final_tasks)


    def __create_buttons_bar(self):
        #region Creación del Frame
        buttons_frame = tk.Frame(self.window, height=100, bg='#AAAAAA')
        # fill='x', hace que el Frame ocupe todo el ancho
        # anchor='n', hace que el Frame se 'ancle' al NORTE (parte superior del contenedor)
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
        self.search_frame = tk.LabelFrame(self.window, bg='#EEEEEE', text='Película', labelanchor=tk.NW)
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

    def __create_menu(self):
        # *** MENÚ PRINCIPAL ***
        # Creación del menú
        self.main_menu = tk.Menu(self.window) 
        # Asignación del menú a la ventana
        self.window.config(menu=self.main_menu) 
        
        # *** MENÚ FILE ***
        # Creación del submenú, sobre el menú principal
        # tearoff=0 --> Elimina una línea discontínua del menú. Probar quitando el atributo.
        self.file_menu = tk.Menu(self.main_menu, tearoff=0) 
        # Asignamos el menú File al menú principal
        self.main_menu.add_cascade(label='File', menu=self.file_menu, underline=0) 

        # *** MENÚ FILE - OPCIONES
        self.file_menu.add_command(label='Open', underline=0, command=self.__show_not_implemented_error)
        self.file_menu.add_command(label='Close', underline=1, command=self.__show_not_implemented_error)
        self.file_menu.add_command(label='Config', underline=2, command=self.__show_not_implemented_error)
        self.file_menu.add_separator() # Dibujar una línea horizontal
        self.file_menu.add_command(label='Exit', underline=0, command=self.__exit_app, accelerator='Ctrl-E')

        self.window.bind_all("<Control-e>", self.__exit_app)


        # *** MENU MOVIES ***
        self.movies_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label='Movies', menu=self.movies_menu, underline=0) 
        
        # *** MENÚ FILE - OPCIONES
        self.movies_menu.add_command(label='Add', underline=0, command=self.__show_not_implemented_error)
        self.movies_menu.add_command(label='View', underline=1, command=self.__show_not_implemented_error)

        # *** MENU HELP ***
        self.help_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label='Help', menu=self.help_menu, underline=0) 

        # *** MENÚ HELP - OPCIONES
        self.help_menu.add_command(label='About...', underline=0, command=self.__show_about)

    def __search_movie(self):
        self.window.config(cursor='clock')
        title = self.e_search_title.get().strip()
        if (title==''):
            self.__show_warning('Debe introducir un título para poder realizar una búsqueda')
            self.e_search_title.focus_set()
        self.window.config(cursor='arrow')

    def __save_movie(self):
        title = self.e_title.get().strip()
        director = self.e_director.get().strip()
        #1.0 Es línea 1, primer carácter
        plot = self.t_plot.get('1.0', tk.END).strip() 
        year = int(self.sp_year.get())
        if (title==''):
            self.__show_warning('No hay datos para almacenar')
            self.e_title.focus_set()
        else:
            print(title, director, plot, year)

    def __exit_app(self, event=None):
        # El objeto event se recibe solo en el caso del bind, no en el command.
        # Si hay que hacer un tratamiento distinto, se debe programar teniendo en
        # cuenta que puede ser None.
        wants_exit = messagebox.askokcancel(SuperMovieGUI.APP_TITLE, '¿Desea salir de la aplicación')
        if (wants_exit):
            # self.window.quit() # Destruye todos los widgets
            self.window.destroy() # Destruye el widget y todos sus descendientes

    def __show_not_implemented_error(self):
        messagebox.showerror(SuperMovieGUI.APP_TITLE, 'Opción no implementada')

    def __show_warning(self, text):
        messagebox.showwarning(SuperMovieGUI.APP_TITLE, text)

    def __show_about(self):
        messagebox.showinfo(SuperMovieGUI.APP_TITLE, 'Versión 1.0. By Fernando Paniagua. 2025.')

    def __do_final_tasks(self):
        print('Haciendo las tareas de cierre de la aplicación...')
        self.window.destroy()