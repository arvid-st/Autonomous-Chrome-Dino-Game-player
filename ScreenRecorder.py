import mss
import mss.tools
import numpy as np
import cv2
import keyboard
import pyautogui as pag

from Coordinates import *

def FullScreenScreenShot():
    full_screen = TakeScreenShot({
        "left": 0,
        "top": 0,
        "width": screenWidth,
        "height": screenHeight
    })
    return full_screen


def TakeScreenShot(region):
    with mss.mss() as sct:
        img = sct.grab(region)
        return cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2BGR)

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

def TakeScreeShotOfScore():
    coordinateArray = [RelativeCoordinateTenThousandScore, RelativeCoordinateThousandScore, RelativeCoordinateHundredScore, RelativeCoordinateTenScore, RelativeCoordinateOneScore]
    grabbedImagesArray = []
    for i in range(0, 5):
        with mss.mss() as sct:
            region = {
                "left": int(coordinateArray[i][0][0]),
                "top": int(coordinateArray[i][0][1]),
                "width": int(coordinateArray[i][1][0] - coordinateArray[i][0][0]),
                "height": int(coordinateArray[i][1][1] - coordinateArray[i][0][1])
            }
            img = sct.grab(region)
            img = cv2.cvtColor(np.array(img), cv2.COLOR_BGRA2BGR)
            grabbedImagesArray.append(img)

    return grabbedImagesArray[0], grabbedImagesArray[1], grabbedImagesArray[2], grabbedImagesArray[3], grabbedImagesArray[4]