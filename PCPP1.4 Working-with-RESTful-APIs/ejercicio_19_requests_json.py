import requests

try:
    reply = requests.get('http://localhost:3000/movies', timeout=0.1)
except requests.exceptions.ConnectionError as ce:
    print('*ConnectionError:', ce)
except Exception as e:
    print('*Exception:', e)
else:
    if (reply.status_code==requests.codes.OK):
        movies = reply.json()
        print(type(movies))
        print(movies)
    else:
        print('Ha pasado algo:', reply.status_code)