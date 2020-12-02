# Author: Alan Licerio
# Course: Theory of Operating Systems
# Assignment: Lab 3 - Threaded Video Player

from FrameQueue import FrameQueue
from methods import extractFiles, convertToGray, display
import threading

VIDEO = "..\clip.mp4" 


if __name__ == "__main__":
    colorFrame = FrameQueue()
    grayFrame = FrameQueue()

    # Threads
    extractThread = threading.Thread(target=extractFiles, args=(VIDEO, colorFrame))
    convertThread = threading.Thread(target=convertToGray, args=(colorFrame, grayFrame))
    displayThread = threading.Thread(target=display, args=(grayFrame,)) #

    # Start Threads
    extractThread.start()
    convertThread.start()
    displayThread.start()