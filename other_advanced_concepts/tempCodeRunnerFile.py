import threading
import time

def my_function():
    print("Start a thread ")
    time.sleep(3)
    print("End a thread ")

threads = []