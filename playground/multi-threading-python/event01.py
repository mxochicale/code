# https://stackoverflow.com/questions/17774768/python-creating-a-shared-variable-between-threads
import threading
import time

c = threading.Condition()
flag = 0  # shared between Thread_A and Thread_B
val = 20


class Thread_A(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global flag
        global val  # made global here
        while True:
            c.acquire()
            if flag == 0:
                print(f'A: val= {str(val)}')
                time.sleep(0.1)
                flag = 1
                val = 30
                c.notify_all()
            else:
                c.wait()
            c.release()


class Thread_B(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global flag
        global val  # made global here
        while True:
            c.acquire()
            if flag == 1:
                print (f'B: val= {str(val)}')
                time.sleep(0.8)
                flag = 0
                val = 20
                c.notify_all()
            else:
                c.wait()
            c.release()


a = Thread_A("myThread_name_A")
b = Thread_B("myThread_name_B")

b.start()
a.start()

a.join()
b.join()
