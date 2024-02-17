from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time, threading
keyboard = KeyboardController()
mouse = MouseController()
def program():

    y = 1
    t1 = 1
    t2 = 1
    keyboard.press('d')
    mouse.press(Button.left)
    for i in range(0, 295):
        keyboard.press(Key.shift)
        time.sleep(t1)
        keyboard.release(Key.shift)
        time.sleep(t2)

    keyboard.release('d')
    mouse.release(Button.left)
    keyboard.press('a')
    mouse.press(Button.left)
    for i in range(0, 295):
        keyboard.press(Key.shift)
        time.sleep(float(t1))
        keyboard.release(Key.shift)
        time.sleep(float(t2))
    keyboard.release('a')
    mouse.release(Button.left)
x = threading.Thread(target=program)
x.start(d)
for i in range(15):
    print("siema")