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
DEBUG = True

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

    ObjectInImage, mask = detectObstacle(obstacleImage, return_mask = True)

    if DEBUG:
        cv2.imshow("Raw obstacle capture", obstacleImage)

        cv2.imshow("Obstacle capture with mask", mask)

        debug_frame = obstacleImage.copy()
        text = "Obstacle detected" if ObjectInImage else "No obstacle"
        color = (0, 0, 255) if ObjectInImage else (0, 255, 0)

        cv2.putText(debug_frame, text, (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        cv2.imshow("Obstacle Debug", debug_frame)

        score_images = TakeScreeShotOfScore()
        for i, img in enumerate(score_images):
            cv2.imshow(f"Score Digit {i}", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            Run = False

cv2.destroyAllWindows()
