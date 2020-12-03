#!/usr/bin/env python3

# Author: Alan Licerio
# Course: Theory of Operating Systems
# Assignment: Lab 3 - Threaded Video Player

import cv2
import threading
from FrameQueue import FrameQueue

VIDEO = "..\clip.mp4" 
DELIMITER = "\0"
DELAY = 42

def extractFiles(filename, outQueue) :
    print('Extracting frames from: ', filename)
    i = 0

    video = cv2.VideoCapture(filename) # Opens the video

    success,image = video.read() # Reads frame

    while success:
        outQueue.enqueue(image)
        success,image = video.read() 
        i+=1 # increment temp variable
    
    outQueue.enqueue(DELIMITER)
    print('Process completed')


def convertToGray(inQueue, outQueue) :
    print("Converting to grayscale...")
    i = 0
    input = inQueue.dequeue()

    while input is not DELIMITER:
        frame = cv2.cvtColor(input, cv2.COLOR_BGR2GRAY) # Conversion to gray
        outQueue.enqueue(frame) # Enqueue frame
        i+=1
        input = inQueue.dequeue() # Dequeue next frame

    outQueue.enqueue(DELIMITER)
    print('Process completed')


def display(frames) :
    print('Displaying frames...')
    i = 0
    frame = frames.dequeue()
    while frame is not DELIMITER:
        cv2.imshow('Video Play', frame)
        if 0xFF == ord("q") and cv2.waitKey(DELAY): # Delay of 42 ms to check if user wants to quit.
            break # Exit loop if condition holds
        i +=1
        frame = frames.dequeue()
    
    cv2.destroyAllWindows() # Cleaning opened windows
    print('Process completed')

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
