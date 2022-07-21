import time
from threading import Thread


def threadFunc(arg1, arg2):
    print(f'Thread arguments=> {arg1} and {arg2}')
    time.sleep(1)  # Seconds
    print(f'End thread function')


thread = Thread(target=threadFunc, args=(100, 200, ))
thread.start()
