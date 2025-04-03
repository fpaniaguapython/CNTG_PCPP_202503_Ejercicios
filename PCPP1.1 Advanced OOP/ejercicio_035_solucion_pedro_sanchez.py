from datetime import datetime

def save(persistence):
   def ext_wrap(func):
       def int_wrap(*args, **kwargs):
           match persistence:
               case 'txt':
                   print('loggin to txt ...')
               case 'db':
                   print('loggin to db ...')
               case 'rest':
                   print('loggin to rest ...')
           return func(*args, **kwargs)
       return int_wrap
   return ext_wrap

@save('txt')
def log(func):
   def wrap(*args, **kwargs):
       print(datetime.now())
       return func(*args, **kwargs)
   return wrap

@log
def hi():
   print('hello world')

hi()