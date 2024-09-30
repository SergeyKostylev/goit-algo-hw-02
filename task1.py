import time
from queue import Queue
from random import randint

queue = Queue()

def generate_request():
    request = randint(1, 1000)
    queue.put(request)

def process_request():
    if queue.empty():
        print("Empty Queue")
    else:
        number = queue.get()
        # processing an application is squaring a number
        print(f"The square root of {number} is {number ** 2}")

while True:
    generate_request()
    process_request()
    time.sleep(0.1)
