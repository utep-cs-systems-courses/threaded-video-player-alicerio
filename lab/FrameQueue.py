# Author: Alan Licerio
# Course: Theory of Operating Systems
# Assignment: Lab 3 - Threaded Video Player

from threading import Semaphore
import threading

class FrameQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()
        self.full = threading.Semaphore(0)
        self.empty = threading.Semaphore(24)

    def enqueue(self, item):
        self.empty.acquire()
        self.lock.acquire() # Makes sure that only one thread access the queue.
        self.queue.append(item)
        self.lock.release()
        self.full.release()

    def dequeue(self):
        self.full.acquire()
        self.lock.acquire()
        item = self.queue.pop(0) # Deletes the first element of the list, transfer it into variable.
        self.lock.release()
        self.empty.release()
        return item