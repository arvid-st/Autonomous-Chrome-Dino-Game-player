import cv2
import numpy as np

def detectObstacle(image, return_mask = False):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # Converts the image from RGB to HSV for better image recognition

    LowerLimitGreenColorArray = [0, 40, 0] # Color can be viewed in Img/HelpToUnderstandImages
    lowerLimitGreen = np.array(LowerLimitGreenColorArray)

    UpperLimitGreenColorArray = [150, 255, 150] # Color can be viewed in Img/HelpToUnderstandImages
    upperLimitGreen = np.array(UpperLimitGreenColorArray)

    mask = cv2.inRange(hsv, lowerLimitGreen, upperLimitGreen) # Creates a black-and-white mask. The marked object
    # (in this case anything green) will be white (255) and anything else, black (0)

    if return_mask:
        return cv2.countNonZero(mask) > 0, mask
    return cv2.countNonZero(mask) > 0 # Counts the pixels marked as white in the mask (aka any green pixels)