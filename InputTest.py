import time
from pynput import keyboard

#fungerar men man måste skapa en virtual environment med 'python3 -m venv venv' i project foldern, aktivera den med 'source venv/bin/activate' samt sedan pynput med pip install 
#Behövs troligen en bättre lösning då denna var lite krånglig.

kb = keyboard.Controller()

stop = False
ducking = False

def jump():
    kb.press(keyboard.Key.space)
    kb.release(keyboard.Key.space)
    print("Jump")

def start_duck():
    global ducking
    if not ducking:
        kb.press(keyboard.Key.down)
        ducking = True
        print("Start duck")

def stop_duck():
    global ducking
    if ducking:
        kb.release(keyboard.Key.down)
        ducking = False
        print("Stop duck")

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
    start_duck()
    time.sleep(0.5)
    stop_duck()
    jump()
    time.sleep(0.5)