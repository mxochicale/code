import time
from threading import Thread


class MyThread(Thread):

    def __init__(self, arg1, arg2):
        super().__init__()
        self.arg1 = arg1
        self.arg2 = arg2

    def run(self):
        print(f'Thread... Passed arguments: {self.arg1} {self.arg2}')
        time.sleep(1)  # Seconds
        print(f'A thread is existing')


mt = MyThread("PASSING_ARG1", 'ARG2')
mt.start()
mt.join()

