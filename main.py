import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time, threading, sys


keyboard = KeyboardController()
mouse = MouseController()
event = threading.Event()

def program():
    print("works")
    y = 1
    if entry.get() == "":
        t1 = 1
        t2 = 1
    else:
        try:
            t1 = float(entry.get())
            t2 = float(entry2.get())
        except:
            t1 = 1
            t2 = 1
    keyboard.press('d')
    mouse.press(Button.left)
    for i in range(0, 295):
        if event.is_set():
            keyboard.release(Key.shift)
            mouse.release(Button.left)
            keyboard.release('d')
            print("!!!!")
            sys.exit(0)
            return
        keyboard.press(Key.shift)
        time.sleep(t1)
        keyboard.release(Key.shift)
        time.sleep(t2)

    keyboard.release('d')
    mouse.release(Button.left)
    keyboard.press('a')
    mouse.press(Button.left)
    for i in range(0, 295):
        if event.is_set():
            keyboard.release(Key.shift)
            mouse.release(Button.left)
            keyboard.release('a')
            print("!!!!")
            sys.exit(0)
            return
        keyboard.press(Key.shift)
        time.sleep(float(t1))
        keyboard.release(Key.shift)
        time.sleep(float(t2))
    keyboard.release('a')
    mouse.release(Button.left)

class Wrapper:
    def __init__(self):
        self.started = False

    def start(self):
        if self.started == False:
            self.z = threading.Thread(target=program, daemon=True)
            self.started = True
            self.z.start()

    def stop(self):
        if self.started == True:
            self.started = False
            self.z = None

my_thread = Wrapper()

def multi():
    event.clear()
    my_thread.start()

def umulti():
    event.set()
    my_thread.stop()
    print("test")


root = ttk.Window(themename="vapor")
root.geometry('600x400')
root.title("RapyClicker v1.0")
root.resizable(0, 0)
b1 = ttk.Button(root, text="Start", bootstyle=SUCCESS, command=multi)
b1.pack(side=BOTTOM, padx=10, pady=10)

b2 = ttk.Button(root, text="Stop", bootstyle=(INFO, OUTLINE), command=umulti)
b2.pack(side=BOTTOM, padx=10, pady=10)

label = ttk.Label(text="Podaj czas A:", font=("Calibri", 11), bootstyle="default")
label.pack()
label.place(relx=0.05, rely=0.05)

entry = ttk.Entry(root)
entry.pack()
entry.place(relx=0.2, rely=0.05)

label2 = ttk.Label(text="Podaj czas B:", font=("Calibri", 11), bootstyle="default")
label2.pack()
label2.place(relx=0.05, rely=0.15)

entry2 = ttk.Entry(root)
entry2.pack()
entry2.place(relx=0.2, rely=0.15)

label2 = ttk.Label(text="Zmieniać channel?", font=("Calibri", 11), bootstyle="default")
label2.pack()
label2.place(relx=0.05, rely=0.25)

toggle = ttk.Checkbutton(bootstyle="success-round-toggle")
toggle.pack()
toggle.place(relx=0.26, rely=0.26)
root.mainloop()