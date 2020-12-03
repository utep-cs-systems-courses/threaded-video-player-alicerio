#!/usr/bin/env python3

# Author: Alan Licerio
# Course: Theory of Operating Systems
# Assignment: Lab 3 - Threaded Video Player

import cv2
import threading
from FrameQueue import FrameQueue 

VIDEO = "../clip.mp4" # video
DELIMITER = "\0"
FRAMEDELAY = 42

# based on extractFrames.py demo
def extractFrames(filename, frameQueue):
    print('Extracting frames from: ', filename)
    i = 0 
    video = cv2.VideoCapture(filename)
    success, image = video.read() # Reading each frame 1 by 1

    print(f'Reading frame {i} {success}')
    while success:
        frameQueue.enqueue(image)

        success, image = video.read()
        i += 1
        print(f'Reading frame {i} {success}')

    print('All frames have been extracted')
    frameQueue.enqueue(DELIMITER)


def convertGrayscale(colorFrames, grayFrames):
    print("Converting to grayscale...")
    i = 0 # initialize frame count

    colorFrame = colorFrames.dequeue()

    while colorFrame is not DELIMITER:
        print(f'Converting frame {i}')

        grayFrame = cv2.cvtColor(colorFrame, cv2.COLOR_BGR2GRAY) # convert the image to grayscale
        grayFrames.enqueue(grayFrame) # enqueue frame 
        i += 1
        colorFrame = colorFrames.obtain() # dequeue next frame

    print('Process completed')
    grayFrames.enqueue(DELIMITER)

def displayFrames(frames):
    print('Displaying frames...')
    i = 0

    frame = frames.dequeue()

    while frame is not DELIMITER:
        print(f'Displaying frame {i}')

        # display the image in a window call "video"
        cv2.imshow('Video Play', frame)

        # wait 42ms (what was used in the demos) and check if the user wants to quit with (q)
        if 0xFF == ord("q") and cv2.waitKey(FRAMEDELAY):
            break
        i += 1
        frame = frames.dequeue()

    cv2.destroyAllWindows() # Cleaning opened windows
    print('Process completed')


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
