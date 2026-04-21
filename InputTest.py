import time
import pyautogui
from pynput import keyboard

#fungerar men man måste skapa en virtual environment med 'python3 -m venv venv' i project foldern, aktivera den med 'source venv/bin/activate' samt sedan ladda ner pyatogui och pynput med pip install 
#Behövs troligen en bättre lösning då denna var lite krånglig.

stop = False

def on_press(key):
    global stop
    try:
        if key.char == 's':
            print("Stopping program")
            stop = True
            return False
    except:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Starting in 5 seconds. Press 's' to stop.")
time.sleep(5)

while not stop:
    pyautogui.press('space')
    time.sleep(1)