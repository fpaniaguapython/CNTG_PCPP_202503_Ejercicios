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
from tkinter import ttk

class SuperMovieGUI:
    APP_TITLE = 'SuperMovie'
    VERSION = '1.0'
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    WINDOW_MIN_WIDTH = 640
    WINDOW_MIN_HEIGHT = 480
    WINDOW_MAX_WIDTH = 1024
    WINDOW_MAX_HEIGHT = 768
    ICON = './icons/icon.png'

    def __init__(self):
        # Ventana principal
        self.__create_window()
        # Frames (no se muestran)
        self.frames = dict() 
        self.frames['create']=self.__create_search_frame()
        self.frames['view']=self.__create_data_table_frame()
        # Menú
        self.__create_menu()
        # Barra de botones
        self.__create_buttons_bar()
        # Mostrar el frame principal
        self.__show_frame(self.frames['create'], fill_method='none', button_frame_enabled=True)
        # Mainloop
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
        self.window.minsize(width=SuperMovieGUI.WINDOW_MIN_WIDTH, height=SuperMovieGUI.WINDOW_MIN_HEIGHT)
        # Restricción de tamaño máximo
        #self.window.maxsize(width=SuperMovieGUI.WINDOW_MAX_WIDTH, height=SuperMovieGUI.WINDOW_MAX_HEIGHT)
        # Restricción de cambio de tamaño
        #self.window.resizable(width=False, height=False)

        # Protocol
        # Intercepta el cierre de la ventana (no el fin de la aplicación)
        self.window.protocol('WM_DELETE_WINDOW', self.__do_final_tasks)

    def __create_buttons_bar(self):
        #region Creación del Frame
        self.buttons_frame = tk.Frame(self.window, height=100, bg='#E0E0E0')
        # fill='x', hace que el Frame ocupe todo el ancho
        # anchor='n', hace que el Frame se 'ancle' al NORTE (parte superior del contenedor)
        self.buttons_frame.pack(fill='x', anchor='n') 
        #endregion

        #region Creación de los botones (dentro del frame)
        self.b_search = tk.Button(self.buttons_frame, text='Buscar', command=self.__search_movie)
        self.search_image = tk.PhotoImage(file="./icons/search.png")
        self.b_search.config(image=self.search_image)
        self.b_search.grid(row=0, column=0)

        self.b_save = tk.Button(self.buttons_frame, text='Guardar', command=self.__save_movie)
        self.save_image = tk.PhotoImage(file="./icons/save.png")
        self.b_save.config(image=self.save_image)
        self.b_save.grid(row=0, column=1)

      
        

        self.all_buttons = []
        self.all_buttons.append(self.b_search)
        self.all_buttons.append(self.b_save)

        #endregion

    def __create_search_frame(self):
        X_LABELS = 50
        X_ENTRIES = 150

        #region Creación del LabelFrame
        self.search_frame = tk.LabelFrame(self.window, bg='#EEEEEE', text='Película', labelanchor=tk.NW)
        # Con esta configuración, el frame ocupa el espacio central
        self.search_frame.config(width=600, height=450)
        # endregion

        #region Creación del Formulario de búsqueda
        self.l_search_title = tk.Label(self.search_frame, text='Título a buscar:')
        self.l_search_title.place(x=50, y=50)

        self.e_search_title = tk.Entry(self.search_frame, width=50)
        self.e_search_title.place(x=X_ENTRIES, y=50)
        

        self.l_title = tk.Label(self.search_frame, text='Título:')
        self.l_director = tk.Label(self.search_frame, text='Director:')
        self.l_plot = tk.Label(self.search_frame, text='Sinopsis:')
        self.l_year = tk.Label(self.search_frame, text='Año de estreno:')

        self.l_title.place(x=X_LABELS, y=100)
        self.l_director.place(x=X_LABELS, y=140)
        self.l_plot.place(x=X_LABELS, y=180)
        self.l_year.place(x=X_LABELS, y=360)

        self.e_title = tk.Entry(self.search_frame, width=50)
        self.e_director = tk.Entry(self.search_frame, width=50)
        self.t_plot = tk.Text(self.search_frame, height=10, width=40)
        self.sp_year = tk.Spinbox(self.search_frame, width=5, from_=1900, to=2025)

        self.e_title.place(x=X_ENTRIES, y=100)
        self.e_director.place(x=X_ENTRIES, y=140)
        self.t_plot.place(x=X_ENTRIES, y=180)
        self.sp_year.place(x=X_ENTRIES, y=360)
        #endregion

        return self.search_frame

    def __create_data_table_frame(self):
        self.data_table_frame = tk.Frame(self.window)
        
        # Tabla
        tree = ttk.Treeview(self.data_table_frame, columns=('Id', 'Title', 'Director', 'Plot', 'Year'), show='headings')
        tree.column('Id', anchor='e', width=30)
        tree.column('Title')
        tree.column('Director', width=50)
        tree.column('Plot')
        tree.column('Year', anchor='e', width=30)

        # Estilos
        style = ttk.Style()
        style.theme_use('default') # default, clam, alt, classic, vista
        style.configure('Treeview',
                        rowheight=30)
        style.configure('Treeview.Heading', 
                        foreground='white',
                        background='#909090',
                        padding=(5, 10))

        # Encabezados
        tree.heading('Id', text='Id')
        tree.heading('Title', text='Título')
        tree.heading('Director', text='Director')
        tree.heading('Plot', text='Sinopsis')
        tree.heading('Year', text='Estreno')
        
        # Datos
        peliculas = [
            (1, 'Tiburón', 'Steven Spielberg', 
            'En la isla turística de Amity, un gigantesco tiburón blanco comienza a atacar a los bañistas. '
            'Un jefe de policía, un biólogo marino y un cazador de tiburones se embarcan en una peligrosa misión para detenerlo.',
            1975),
            
            (2, 'Alien, el octavo pasajero', 'Ridley Scott',  
            'La tripulación de la nave Nostromo recibe una señal de auxilio desde un planeta desconocido. '
            'Al investigar, descubren una forma de vida alienígena letal que comienza a acecharlos dentro de la nave.',
            1979),
            
            (3, 'Alguien voló sobre el nido del cuco', 'Miloš Forman',
            'Randle McMurphy, un hombre rebelde, es internado en un hospital psiquiátrico, donde se enfrenta a la estricta enfermera Ratched. '
            'Su espíritu de libertad inspira a los otros pacientes, generando un choque de poder dentro de la institución.',
            1975)
        ]

        for fila in peliculas:
            tree.insert('', 'end', values=fila)

        # Posicionamiento de la tabla
        tree.pack(expand=True, fill='both')

        return self.data_table_frame

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

        self.window.bind_all('<Control-e>', self.__exit_app)


        # *** MENU MOVIES ***
        self.movies_menu = tk.Menu(self.main_menu, tearoff=0)
        self.main_menu.add_cascade(label='Movies', menu=self.movies_menu, underline=0) 
        
        # *** MENÚ FILE - OPCIONES
        self.movies_menu.add_command(label='Add', underline=0, 
            command= lambda target = self.frames['create'] : self.__show_frame(target, fill_method='none', button_frame_enabled=True))
        self.movies_menu.add_command(label='View', underline=1, 
            command= lambda target = self.frames['view'] : self.__show_frame(target, fill_method='both', button_frame_enabled=False))

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

    def __show_frame(self, current_frame, fill_method, button_frame_enabled):
        # Ocultar la barra de herramientas o desactivar los botones
        if button_frame_enabled:
            # Opción 1. Mostrar
            # self.buttons_frame.pack(fill='x', anchor='n') 

            # Opción 2. Activar
            list(map(lambda boton : boton.config(state='active'), self.all_buttons))
        else:
            # Opción 1. Ocultar
            # self.buttons_frame.forget()

            # Opción 2. Desactivar
            list(map(lambda boton : boton.config(state='disabled'), self.all_buttons))
        
        # Ocultar todos los frames
        for frame in self.frames.values():
            frame.pack_forget()

        # Mostrar el frame activo        
        current_frame.pack(fill=fill_method, expand=True)        