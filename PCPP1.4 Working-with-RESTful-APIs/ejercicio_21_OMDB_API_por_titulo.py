import requests
# Por ahorrar tiempo y espacio no se gestionan los errores (habría que hacerlo)
# http://www.omdbapi.com/?apikey=95c08eba&t=Superman
API_KEY = '95c08eba'
URL = 'https://www.omdbapi.com/'

def show_movie(movie):
    print(movie['Title'])

def read(title):
    # Params
    request_params = {'apikey':API_KEY, 't':title}
    reply = requests.get(URL, params=request_params)
    
    if (reply.status_code==requests.codes.OK):
        movie = reply.json()
        show_movie(movie)
    else:
        print('Ha pasado algo:', reply.status_code)

if __name__=='__main__':
    title = input('Introduce un título de película:')
    read(title)