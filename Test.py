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

Run = True

def TakeScreenShotAtSecionOfScreen(top_left, bottom_right, name = None):
    with mss.mss() as sct:
        region = {
            "left": int(top_left[0]),
            "top": int(top_left[1]),
            "width": int(bottom_right[0] - top_left[0]),
            "height": int(bottom_right[1] - top_left[1])
        }

        img = sct.grab(region)
        if name != None:
            mss.tools.to_png(img.rgb, img.size, output = name + ".png")

        return cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2BGR)

while Run:
    if keyboard.is_pressed('s'):
        Run = False

    if keyboard.is_pressed('space'):
        a = (RelativeCoordinateScoreTopLeft[0] - 2,) + RelativeCoordinateScoreTopLeft[1:]
        b = (RelativeCoordinateScoreBottomRight[0] - 2,) + RelativeCoordinateScoreBottomRight[1:]
        TakeScreenShotAtSecionOfScreen(a, b, "score1")
        print(RelativeCoordinateScoreTopLeft)
        print(RelativeCoordinateScoreBottomRight)

        TakeScreenShotAtSecionOfScreen((979,316), (1032, 327), "score")
