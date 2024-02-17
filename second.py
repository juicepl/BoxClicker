from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time
keyboard = KeyboardController()
mouse = MouseController()
t1 = input("Jaka ma być rożnica pomiędzy kliknięciem, a odkliknięciem shifta? Pozostaw puste pole, jeśli chcesz zachować domyślne wartości. ")
t2 = input("Jaka ma być rożnica pomiędzy odkliknięciem, a następnym klikjnięciem shifta? Pozostaw puste pole, jeśli chcesz zachować domyślne wartości. ")
y=1
if t1=="":
    x=1
else:
    try:
        x = float(t1)
    except:
        print("Niepoprawny argument/y")
        y=0
if t2=="":
    x=0.3
else:
    if y==1:
        try:
            x = float(t2)
        except:
            print("Niepoprawny argument/y")
            y=0
if y==1:
    print("")
    print("Włączenie programu nastąpi za 5 sekund.")
    time.sleep(5)
while y==1:
    keyboard.press('d')
    mouse.press(Button.left)
    for i in range(0,295):
        keyboard.press(Key.shift)
        time.sleep(float(x))
        keyboard.release(Key.shift)
        time.sleep(float(y))

    keyboard.release('d')
    mouse.release(Button.left)
    '''keyboard.type('/')
    time.sleep(0.1)
    keyboard.type('ch')
    mouse.position = (852, 376)
    mouse.press(Button.left)
    mouse.release(Button.left)
'''
    keyboard.press('a')
    mouse.press(Button.left)
    for i in range(0,295):
        keyboard.press(Key.shift)
        time.sleep(float(t1))
        keyboard.release(Key.shift)
        time.sleep(float(t2))
    keyboard.release('a')
    mouse.release(Button.left)
    '''keyboard.type('/')
    time.sleep(0.1)
    keyboard.type('ch')
    mouse.position = (852, 376)
    mouse.press(Button.left)
    mouse.release(Button.left)'''