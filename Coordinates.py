import pyautogui as pag
import numpy as np
import cv2


def findDino(frame):
    template = cv2.imread("Img/Dino2.png", cv2.IMREAD_GRAYSCALE)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    best_match = None
    best_val = 0

    candidates = []

    for scale in np.linspace(0.5, 1.5, 20):
        resized = cv2.resize(template, None, fx=scale, fy=scale)
        h, w = resized.shape

        if h > gray.shape[0] or w > gray.shape[1]:
            continue

        result = cv2.matchTemplate(gray, resized, cv2.TM_CCOEFF_NORMED)

        locations = np.where(result >= 0.5)

        for pt in zip(*locations[::-1]):
            candidates.append((pt[0], pt[1], w, h))

    # pick the lowest dino
    if not candidates:
        return None

    best = max(candidates, key=lambda c: c[1])  # largest y = lowest
    return best


def computeObstacleROI(dino):
    x, y, w, h = dino

    return {
        "left": int(x + w * 1.5),
        "top": int(y),
        "width": int(w * 4),
        "height": int(h * 1.5)
    }

def compute_obstacle_roi_local(dino_local):
    x, y, w, h = dino_local

    return {
        "left": int(x + w * 1.5),
        "top": int(y),
        "width": int(w * 4),
        "height": int(h * 1.5)
    }

def compute_game_region(dino, screenWidth, screenHeight):
    x, y, w, h = dino

    left = int(x - w * 2)
    top = int(y - h * 2)
    width = int(w * 12)
    height = int(h * 5)

    left = max(0, left)
    top = max(0, top)

    width = min(width, screenWidth - left)
    height = min(height, screenHeight - top)

    return {
        "left": left,
        "top": top,
        "width": width,
        "height": height
    }


screenWidth, screenHeight = pag.size()

