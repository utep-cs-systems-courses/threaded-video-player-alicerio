#!/usr/bin/env python3

# Author: Alan Licerio
# Course: Theory of Operating Systems
# Assignment: Lab 3 - Threaded Video Player

import threading
from FrameQueue import FrameQueue 
from methods import extractFrames, convertGrayscale, displayFrames

VIDEO = "../clip.mp4" # video

if __name__ == "__main__":

    colorFrames = FrameQueue()
    grayFrames = FrameQueue()

    extractThread = threading.Thread(target = extractFrames, args = (VIDEO, colorFrames))
    convertThread = threading.Thread(target = convertGrayscale, args = (colorFrames, grayFrames))
    displayThread = threading.Thread(target = displayFrames, args = (grayFrames,)) #

    # Start Threads
    extractThread.start()
    convertThread.start()
    displayThread.start()
