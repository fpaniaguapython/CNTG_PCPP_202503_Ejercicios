import requests
import json
# Por ahorrar tiempo y espacio no se gestionan los errores (habría que hacerlo)

def get_new_movie(id):
    '''
    Proporciona un JSON con los datos de una película ficticia
    '''
    new_movie = {
        "id": str(id),
        "Title": "Película nueva",
        "Year": "2009",
        "Rated": "PG-13",
        "Released": "18 Dec 2009",
        "Runtime": "162 min",
        "Genre": "Action, Adventure, Fantasy",
        "Director": "James Cameron",
        "Writer": "James Cameron",
        "Actors": "Sam Worthington, Zoe Saldana, Sigourney Weaver, Stephen Lang",
        "Plot": "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "Language": "English, Spanish",
        "Country": "USA, UK",
        "Awards": "Won 3 Oscars. Another 80 wins & 121 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg",
        "Metascore": "83",
        "imdbRating": "7.9",
        "imdbVotes": "890,617",
        "imdbID": "tt0499549",
        "Type": "movie",
        "Response": "True",
        "Images": [
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyOTYyMzUxNl5BMl5BanBnXkFtZTcwNTg0MTUzNA@@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BNzM2MDk3MTcyMV5BMl5BanBnXkFtZTcwNjg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2ODQ3NjMyMl5BMl5BanBnXkFtZTcwODg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxOTEwNDcxN15BMl5BanBnXkFtZTcwOTg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxMDg1Nzk1MV5BMl5BanBnXkFtZTcwMDk0MTUzNA@@._V1_SX1500_CR0,0,1500,999_AL_.jpg"
        ]
        }
    return new_movie

def get_updated_movie(id):
    '''
    Proporciona un JSON con los datos de una película ficticia MODIFICADA
    '''
    updated_movie = {
        "id": str(id),
        "Title": "Película MODIFICADA",
        "Year": "2009",
        "Rated": "PG-13",
        "Released": "18 Dec 2009",
        "Runtime": "162 min",
        "Genre": "Action, Adventure, Fantasy",
        "Director": "James Cameron",
        "Writer": "James Cameron",
        "Actors": "Sam Worthington, Zoe Saldana, Sigourney Weaver, Stephen Lang",
        "Plot": "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
        "Language": "English, Spanish",
        "Country": "USA, UK",
        "Awards": "Won 3 Oscars. Another 80 wins & 121 nominations.",
        "Poster": "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SX300.jpg",
        "Metascore": "83",
        "imdbRating": "7.9",
        "imdbVotes": "890,617",
        "imdbID": "tt0499549",
        "Type": "movie",
        "Response": "True",
        "Images": [
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEyOTYyMzUxNl5BMl5BanBnXkFtZTcwNTg0MTUzNA@@._V1_SX1500_CR0,0,1500,999_AL_.jpg",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BNzM2MDk3MTcyMV5BMl5BanBnXkFtZTcwNjg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY2ODQ3NjMyMl5BMl5BanBnXkFtZTcwODg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxOTEwNDcxN15BMl5BanBnXkFtZTcwOTg0MTUzNA@@._V1_SX1777_CR0,0,1777,999_AL_.jpg",
            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxMDg1Nzk1MV5BMl5BanBnXkFtZTcwMDk0MTUzNA@@._V1_SX1500_CR0,0,1500,999_AL_.jpg"
        ]
        }
    return updated_movie

def show_movies(movies):
    for movie in movies:
        show_movie(movie)

def show_movie(movie):
    print(movie['Title'])

def create(id):
    # Especificación del tipo de contenido
    h_content = {'Content-type': 'aplication/json'}
    # Conversión del diccionario con los datos a un objeto serializado
    send_data = json.dumps(get_new_movie(id))
    reply = requests.post('http://localhost:3000/movies', headers=h_content, data=send_data)
    if (reply.status_code==requests.codes.created):
        print('La película se ha creado correctamente')
    else:
        print('Ha pasado algo:', reply.status_code)

def read():
    reply = requests.get('http://localhost:3000/movies/5')
    if (reply.status_code==requests.codes.OK):
        movie = reply.json()
        show_movie(movie)
    else:
        print('Ha pasado algo:', reply.status_code)

def read_all():
    reply = requests.get('http://localhost:3000/movies/', timeout=0.1)
    if (reply.status_code==requests.codes.OK):
        movies = reply.json()
        show_movies(movies)
    else:
        print('Ha pasado algo:', reply.status_code)

def update(id):
    h_content = {'Content-type': 'aplication/json'}
    send_data = json.dumps(get_updated_movie(id))
    reply = requests.put(f'http://localhost:3000/movies/{id}', headers=h_content, data=send_data)
    if (reply.status_code==requests.codes.ok):
        print('La película se ha modificado correctamente')
    else:
        print('Ha pasado algo:', reply.status_code)

def delete(id):
    h_content = {'Content-type': 'aplication/json'}
    reply = requests.delete(f'http://localhost:3000/movies/{id}', headers=h_content)
    if (reply.status_code==requests.codes.ok):
        print('La película se ha borrado correctamente')
    else:
        print('Ha pasado algo:', reply.status_code)

if __name__=='__main__':
    #read()
    #read_all()
    #create(21)
    #update(21)
    delete(21)