#!/usr/bin/env python3

# Author: Alan Licerio
# Course: Theory of Operating Systems
# Assignment: Lab 3 - Threaded Video Player

import cv2
from FrameQueue import FrameQueue 

VIDEO = "../clip.mp4" # video
FRAMEDELAY = 42

def extractFrames(filename, frameQueue):
    print('Extracting frames from: ', filename)
    i = 0 
    video = cv2.VideoCapture(filename)
    success, image = video.read() # Reading each frame 1 by 1

    print('Extracted Frame # {i}')
    
    while success:
        frameQueue.enqueue(image)
        success, image = video.read()
        i += 1
        print(f'Frame # {i} enqueued')

    print('Frame extraction completed')
    frameQueue.enqueue(None)


def convertGrayscale(colorFrames, grayFrames):
    print("Converting to grayscale...")
    i = 0
    colorFrame = colorFrames.dequeue()

    while colorFrame is not None:
        print(f'Converting frame # {i}')

        grayFrame = cv2.cvtColor(colorFrame, cv2.COLOR_BGR2GRAY) # convert the image to grayscale
        grayFrames.enqueue(grayFrame) # enqueue frame 
        i += 1
        colorFrame = colorFrames.dequeue() # dequeue next frame

    print('Frame conversion completed')
    grayFrames.enqueue(None)

def displayFrames(frames):
    print('Displaying frames...')
    i = 0

    frame = frames.dequeue()

    while frame is not None:
        print(f'Displaying frame # {i}')
        cv2.imshow('Video Play', frame)

        if cv2.waitKey(FRAMEDELAY) and 0xFF == ord("q"):
            break

        i += 1
        frame = frames.dequeue()

    print('Frame displaying completed.')
    cv2.destroyAllWindows() # Cleaning opened windows
