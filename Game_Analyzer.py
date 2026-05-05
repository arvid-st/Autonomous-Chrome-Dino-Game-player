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


DEBUG = True
Run = True


# Setup debug windows
if DEBUG:
    cv2.namedWindow("Debug", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Debug", 800, 400)
    cv2.moveWindow("Debug", 50, 50)

# Detect dino (fullscreen)
dino = None

while dino is None:
    frame = FullScreenScreenShot()
    dino = findDino(frame)

    if DEBUG:
        debug_frame = frame.copy()

        if dino:
            x, y, w, h = dino
            cv2.rectangle(debug_frame, (x, y), (x+w, y+h), (0,255,0), 2)

        small = cv2.resize(debug_frame, (800, 400))
        cv2.imshow("Debug", small)
        cv2.waitKey(1)

print("Dino detected:", dino)

# Compute game region ONCE
game_region = compute_game_region(dino, screenWidth, screenHeight)

# Convert dino → local coords
dino_local = (
    dino[0] - game_region["left"],
    dino[1] - game_region["top"],
    dino[2],
    dino[3]
)

# Precompute ROI (local)
roi_local = compute_obstacle_roi_local(dino_local)


# Main loop (cropped capture)
while Run:
    if keyboard.is_pressed('s'):
        Run = False

    # capture ONLY game region
    frame = TakeScreenShot(game_region)

    # crop obstacle ROI from frame
    x = roi_local["left"]
    y = roi_local["top"]
    w = roi_local["width"]
    h = roi_local["height"]

    obstacleImage = frame[y:y+h, x:x+w]

    ObjectInImage, mask = detectObstacle(obstacleImage, return_mask=True)


    # DEBUG VISUALIZATION
    if DEBUG:
        debug_frame = frame.copy()

        # draw dino
        dx, dy, dw, dh = dino_local
        cv2.rectangle(debug_frame, (dx, dy), (dx+dw, dy+dh), (0,255,0), 2)

        # draw ROI
        cv2.rectangle(
            debug_frame,
            (x, y),
            (x+w, y+h),
            (255, 0, 0), 2
        )

        # detection text
        text = "DETECTED" if ObjectInImage else "CLEAR"
        color = (0,0,255) if ObjectInImage else (0,255,0)

        cv2.putText(debug_frame, text, (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        small = cv2.resize(debug_frame, (800, 400))
        cv2.imshow("Debug", small)

        cv2.waitKey(1)

cv2.destroyAllWindows()