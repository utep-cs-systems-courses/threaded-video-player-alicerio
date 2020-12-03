# Author: Alan Licerio
# Course: Theory of Operating Systems
# Assignment: Lab 3 - Threaded Video Player

import threading

class FrameQueue():
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()
        self.full = threading.Semaphore(0)
        self.empty = threading.Semaphore(24)

    def enqueue(self, frame):
        self.empty.acquire()
        self.lock.acquire() # Makes sure that only one thread access the queue.
        self.queue.append(frame)
        self.lock.release()
        self.full.release()

    def dequeue(self):
        self.full.acquire()
        self.lock.acquire()
        frame = self.queue.pop(0) # Deletes the first element of the list, transfer it into variable.
        self.lock.release()
        self.empty.release()
        return frame