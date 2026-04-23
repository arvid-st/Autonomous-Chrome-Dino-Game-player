import cv2
import numpy as np

ObjectAlreadyInImage = False

def detectObstacle(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    LowerLimitGreenColorArray = [0, 40, 0]
    lowerLimitGreen = np.array(LowerLimitGreenColorArray)

    UpperLimitGreenColorArray = [150, 255, 150]
    upperLimitGreen = np.array(UpperLimitGreenColorArray)

    mask = cv2.inRange(hsv, lowerLimitGreen, upperLimitGreen)

    return cv2.countNonZero(mask) > 0