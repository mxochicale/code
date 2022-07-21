import time
from threading import Thread


def threadFunc():
    print(f'Start thread function')
    time.sleep(1) # Seconds
    print(f'End thread function')


thread = Thread(target=threadFunc)
thread.is_alive()
thread.start()
thread.join()
print(f'thread.name: {thread.name}')

thread = Thread(target=threadFunc, name='Learning Threads')
thread.is_alive()
thread.start()
thread.join()
print(f'thread.name: {thread.name}')

##Identity
thread = Thread(target=threadFunc)
print(thread.ident)
thread.start()
print(thread.ident)

## Check if a thread is already excecuted
thread.ident != None and thread.is_alive() == False






