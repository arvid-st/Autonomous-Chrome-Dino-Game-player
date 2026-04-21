import mss
import mss.tools
import numpy as np
import cv2
import keyboard
import pyautogui as pag

spaceIsNotPressed = True

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

while spaceIsNotPressed:
    if keyboard.is_pressed('space'):
        spaceIsNotPressed = False
        TakeScreenShotAtSecionOfScreen((0, 0), (screen_width, screen_height),"entireScreen")  # in this case screenshot the section "entire screen"

        TakeScreenShotAtSecionOfScreen((1214, 313), (1277, 328), "Score")
        # Top left: Point(x=1214, y=313)
        # Bottom right: Point(x=1277, y=328)

