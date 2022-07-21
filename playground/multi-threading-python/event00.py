# https://stackoverflow.com/questions/17774768/python-creating-a-shared-variable-between-threads
# "For example in the script below, worker1 and worker2 share
# an Event, and when worker2 changes its value this is seen by worker1"

import time
from threading import Thread, Event

shared_bool = Event()


def worker1(shared_bool):
    while True:
        if shared_bool.is_set():
            print("value is True, quitting")
            return
        else:
            print("value is False")
        time.sleep(1)


def worker2(shared_bool):
    time.sleep(1.5)
    shared_bool.set()


t1 = Thread(target=worker1, args=(shared_bool,))
t2 = Thread(target=worker2, args=(shared_bool,))
t1.start()
t2.start()
t1.join()
t2.join()
