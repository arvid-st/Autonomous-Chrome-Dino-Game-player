import mss
import mss.tools
import numpy as np
import cv2
import keyboard
import pyautogui as pag

from ScreenRecorder import *
from ObstacleDetection import *
from Coordinates import *
from ScoreDetector import *

WaitForRun = True
Run = True
ObjectAlreadyInImage = False
AmountOfObjectsDetected = 0

while WaitForRun:
    if keyboard.is_pressed('s'):
        WaitForRun = False

    if keyboard.is_pressed('space'):
        run = True
        WaitForRun = False

while Run:
    if keyboard.is_pressed('s'):
        Run = False

    obstacleImage = TakeScreenShotAtSecionOfScreen(RelativeCoordinateObstacleTopLeft, RelativeCoordinateObstacleBottomRight)

    ObjectInImage = detectObstacle(obstacleImage)

    if ObjectInImage and not ObjectAlreadyInImage: # This makes the code only capture the same object once
        AmountOfObjectsDetected += 1
        print("Detected obstacle")

        TakeScreenShotAtSecionOfScreen(RelativeCoordinateScoreTopLeft, RelativeCoordinateScoreBottomRight, "Score" + str(AmountOfObjectsDetected)) # Only Score needs to be captured as an image.
        print("Score" + str(AmountOfObjectsDetected) + ": " + str(DetectScore(*TakeScreeShotOfScore())))

    ObjectAlreadyInImage = ObjectInImage
