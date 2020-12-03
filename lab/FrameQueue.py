# Author: Alan Licerio
# Course: Theory of Operating Systems
# Assignment: Lab 3 - Threaded Video Player

from threading import Semaphore
import threading

class FrameQueue:
    def __init__(self):
        self.queue = []
        self.queueLock = threading.Lock()
        self.emptyCheck = threading.Semaphore(0)
        self.fullCheck = threading.Semaphore(24)

    def enqueue(self, frame):
        self.emptyCheck.acquire() 
        self.queueLock.acquire() # Makes sure that only one thread access the queue.
        self.queue.append(frame)
        self.queueLock.release()    
        self.fullCheck.release()

    def dequeue(self):
        self.fullCheck.acquire()
        self.queueLock.acquire()
        frame = self.queue.pop(0) # Deletes the first element of the list, transfer it into variable.
        self.queueLock.release()
        self.emptyCheck.release() # Unlocks the producer thread if there is space left in the queue.
        return frame
