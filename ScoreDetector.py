import mss
import mss.tools
import numpy as np
import cv2
import keyboard
import pyautogui as pag


def DetectScore(TenThousandImage, ThousandImage, HundredImage, TenImage, OneImage):
    return GetNumberFromImage(TenThousandImage) * 10000 + GetNumberFromImage(ThousandImage) * 1000 + GetNumberFromImage(HundredImage) * 100 + GetNumberFromImage(TenImage) * 10 + GetNumberFromImage(OneImage)

def GetNumberFromImage(image):
    ImageArray = ["Zero.jpg", "One.jpg", "Two.jpg", "Three.jpg", "Four.jpg", "Five.jpg", "Six.jpg", "Seven.jpg", "Eight.jpg", "Nine.jpg"]
    FoundAMatch = False

    for i in range(0,10):
        if imageDifferencePercent(createScoreMask(image), ImageArray[i]) < 50:
            return i
    raise Exception("Found no image match from score...")

def imageDifferencePercent(image1, image2):
    image2 = cv2.imread("Img/Score/" + image2)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    if image1.shape != image2.shape:
        image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

    difference = cv2.absdiff(image1, image2)

    changedPixels = cv2.countNonZero(difference)
    totalPixels = difference.shape[0] * difference.shape[1]

    return changedPixels / totalPixels * 100

def createScoreMask(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) # Makes all pixels under 127 grayscale brightness black, and all over 127 white.
    return mask

print(DetectScore(cv2.imread("Img/Score/Two.jpg"),cv2.imread("Img/Score/One.jpg"),cv2.imread("Img/Score/Two.jpg"),cv2.imread("Img/Score/One.jpg"),cv2.imread("Img/Score/One.jpg")))