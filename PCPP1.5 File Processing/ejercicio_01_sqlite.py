import sqlite3

class Movie:
    def __init__(self, id, title, director, year):
        self.id = id
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f'Id:{self.id}. Title:{self.title}. Director:{self.director}. Year:{self.year}'


class BaseDatosPeliculas:
    # CONSTRUCTOR
    def __init__(self):
        print('Abriendo la conexión...')
        self.conn = sqlite3.connect('movies.db')
        self.__create_table()
    
    # CREACIÓN DEL MODELO DE DATOS
    def __create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS movies  (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL,
                       director TEXT NOT NULL,
                       year INTEGER NOT NULL)
        """)
        self.conn.commit()

    # CRUD
    # CREATE
    def insert_movie(self, movie : Movie):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO movies (title, director, year) VALUES (?,?,?)',
                       (movie.title, movie.director, movie.year))
        self.conn.commit()

    # READ ALL
    # Opción 1. Devuelve una lista con todos los elementos. Usamos fechone
    # def read_movies(self):
    #     cursor = self.conn.cursor()
    #     cursor.execute('SELECT * FROM movies')
    #     movies = []
    #     while True:
    #         movie = cursor.fetchone()
    #         if movie==None:
    #             break
    #         movies.append(Movie(*movie))
    #     return movies

    # Opción 2. Devuelve una lista con todos los elementos. Usamos fechall
    # def read_movies(self):
    #     cursor = self.conn.cursor()
    #     cursor.execute('SELECT * FROM movies')
    #     movies_db = []
    #     movies_db = cursor.fetchall()
    #     movies = []
    #     for movie in movies_db:
    #         movies.append(Movie(*movie))
    #     return movies

    # Opción 3. Devuelve una lista con todos los elementos. 
    # Usamos fechall y comprensión de listas (M. Souto)
    # def read_movies(self):
    #     cursor = self.conn.cursor()
    #     cursor.execute("SELECT * FROM movies")
    #     movies = cursor.fetchall()
    #     return [Movie(*movie) for movie in movies] 

    # Opción 4. Devuelve el cursor (J.L. Varela)
    # def read_movies(self):
    #     cursor = self.conn.cursor()
    #     movies = cursor.execute('SELECT * FROM movies');
    #     return movies


    # READ ONE
    def read_movie(self, id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM movies WHERE id=?",(id,))
        movie = cursor.fetchone()
        if (movie==None):
            raise IndexError('No se ha encontrado la película')
        movies = Movie(*movie)
        cursor.close()
        return movies

    # UPDATE 
    def update_movie(self, movie):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE movies SET title=? where id=?", (movie.title, movie.id))
        cursor.close()
        self.conn.commit()
    
    # DELETE
    def delete_movie(self, id):
        cursor = self.conn.cursor()
        result = cursor.execute("DELETE FROM movies WHERE id=?", (id,))
        cursor.close()
        self.conn.commit()
        return result.rowcount

    # DESTRUCTOR
    def __del__(self):
        print('Cerrando la conexión...')
        self.conn.close()
    

movies_db = BaseDatosPeliculas()
# tiburon = Movie(0, 'Tiburón II', 'Steven Spielberg', 1979)

# CREATE
# movies_db.insert_movie(tiburon)

# READ ALL
# movies = movies_db.read_movies()
# for movie in movies:
#     print(movie)

# READ ONE
# try:
#     movie = movies_db.read_movie(2)
# except IndexError as ie:
#     print(ie)
# else:
#     print(movie)

# UPDATE
# pelicula = movies_db.read_movie(2)
# pelicula.title = 'Modificado'
# movies_db.update_movie(pelicula)

# DELETE
rowcount = movies_db.delete_movie(1)
if (rowcount==0):
    print('No se ha borrado nada')
else:
    print('El registro se ha borrado satisfactoriamente')