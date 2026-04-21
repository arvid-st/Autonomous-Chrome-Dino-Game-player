import keyboard
import pyautogui as pag

spaceIsNotPressed = True 

def returnMousePosition():
    return pag.position()

while spaceIsNotPressed:
    if keyboard.is_pressed('space'):
        spaceIsNotPressed = False
        print(returnMousePosition())