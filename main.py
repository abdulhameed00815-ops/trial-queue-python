import threading
import time
from queue import Queue

q = Queue(maxsize=6)

def say_hi():
    print("hi!")


def say_fuck_you():
    print("fuck you!")


def say_stfu():
    print("stfu!")


def producer():
    while True:
        task = input("Enter function name: ")
        if task == "say_hi":
            q.put(say_hi)
        elif task == "say_fuck_you":
            q.put(say_fuck_you)
        elif task == "say_stfu":
            q.put(say_stfu)
        time.sleep(1)


threading.Thread(target=producer).start()


def consumer():
    while True:
        try:
            dequeue_task = q.get()
            dequeue_task()
        except IndexError:
            continue
        
        
#the code below gets executed if the code is run directly using "python3 main.py".
if __name__ == '__main__':
    consumer()
