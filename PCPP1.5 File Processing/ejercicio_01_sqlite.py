import sqlite3

class Movie:
    def __init__(self, id, title, director, year):
        self.id = id
        self.title = title
        self.director = director
        self.year = year


class BaseDatosPeliculas:
    def __init__(self):
        self.conn = sqlite3.connect('movies.db')
        self.__create_table()
    
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


    # READ ONE

    

movies_db = BaseDatosPeliculas()
tiburon = Movie(0, 'Tiburón II', 'Steven Spielberg', 1979)
movies_db.insert_movie(tiburon)

