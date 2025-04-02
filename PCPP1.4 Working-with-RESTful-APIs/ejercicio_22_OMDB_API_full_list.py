import requests
# Por ahorrar tiempo y espacio no se gestionan los errores (habría que hacerlo)
# http://www.omdbapi.com/?apikey=95c08eba&s=Superman
API_KEY = '95c08eba'
URL = 'https://www.omdbapi.com/'
MOVIES_PER_PAGE = 10

def show_movie(movie):
    print(movie['Title'])

def show_page(movies):
    for movie in movies:
        show_movie(movie)

def find_all(title, current_page):
    request_params = {'apikey':API_KEY, 's':title, 'page':current_page}
    reply = requests.get(URL, params=request_params)
    if (reply.status_code==requests.codes.OK):
        result = reply.json()
        total_results = int(result['totalResults']) # Número de registros
        total_pages = total_results / MOVIES_PER_PAGE
        data = result['Search']
        show_page(data)
        current_page+=1
        if (current_page>total_pages):
            return
        find_all(title, current_page)
    else:
        print('Ha pasado algo:', reply.status_code)
    

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
    find_all(title, 1)