import mss
import mss.tools
import numpy as np
import cv2
import keyboard
import pyautogui as pag

import ObstacleDetection

Run = True
ObjectAlreadyInImage = False
AmountOfObjectsDetected = 0

def GetScreenResolution():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        return monitor["width"], monitor["height"]

def TakeScreenShotAtSecionOfScreen(top_left, bottom_right, outputImageName):
    with mss.mss() as sct:
        region = {
            "left": top_left[0],
            "top": top_left[1],
            "width": bottom_right[0] - top_left[0],
            "height": bottom_right[1] - top_left[1]
        }

        img = sct.grab(region)
        mss.tools.to_png(img.rgb, img.size, output = outputImageName + ".png")

screen_width, screen_height = GetScreenResolution()

print(screen_width)
print(screen_height)

while Run:
    if keyboard.is_pressed('s'):
        Run = False

    TakeScreenShotAtSecionOfScreen((1190, 387), (1290, 465), "ObstacleCapture")

    ObjectInImage = ObstacleDetection.detectObstacle(cv2.imread("ObstacleCapture.png"))

    if ObjectInImage and not ObjectAlreadyInImage:
        AmountOfObjectsDetected += 1
        print("Detected obstacle")
        TakeScreenShotAtSecionOfScreen((0, 0), (screen_width, screen_height),
                                       "entireScreen" + str(AmountOfObjectsDetected))  # in this case screenshot the section "entire screen"

        TakeScreenShotAtSecionOfScreen((1219, 316), (1273, 326), "Score" + str(AmountOfObjectsDetected))
        # Top left: Point(x=1219, y=316)
        # Bottom right: Point(x=1273, y=326)

        TakeScreenShotAtSecionOfScreen((1190, 387), (1290, 465), "ObstacleCaptured" + str(AmountOfObjectsDetected))
        # Top left: Point(x=1190, y=387)
        # Bottom right: Point(x=1290, y=465)
    ObjectAlreadyInImage = ObjectInImage
