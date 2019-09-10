import threading
from time import sleep
from datetime import datetime

def hello(thread_id):
    print('{}: Hello, World! for the first time from thread {}: sleeping for 1 second'.format(datetime.now(),thread_id))
    sleep(1)
    print('{}: Hello, World! for the second time from thread {}: sleeping for 1 second'.format(datetime.now(),thread_id))
    sleep(1)
    print('{}: Hello, World! for the third time from thread {}: sleeping for 1 second'.format(datetime.now(),thread_id))
    sleep(1)
    print('Thread {} has ended'.format(thread_id))
    return

if __name__ == '__main__':
    num_threads = 5
    print('Starting {} threads, 500ms apart'.format(num_threads))
    for i in range(num_threads):
        thread = threading.Thread(target=hello, args=(i+1,))
        sleep(0.5)
        print('{}: Thread {} is starting'.format(datetime.now(),i+1))
        thread.start()