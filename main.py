from tkinter import *
import pyautogui
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time, threading, sys
keyboard = KeyboardController()
mouse = MouseController()
event = threading.Event()


def program():
    time.sleep(3)
    print(channel.get())
    print("works")
    y = 1
    if entry.get() == "":
        t1 = 0.05
        t2 = 0.7
    else:
        try:
            t1 = float(entry.get())
            t2 = float(entry2.get())
        except:
            t1 = 0.05
            t2 = 0.1
    while not event.is_set():
        time.sleep(3)
        keyboard.press('d')
        mouse.press(Button.left)
        for i in range(0, 70):
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
        time.sleep(0.2)
        keyboard.release('d')
        mouse.release(Button.left)
        if channel.get() == 1:
            if my_thread.n == 9:
                my_thread.n = 0
            cpath = ["images/ch1.png", "images/ch2.png", "images/ch3.png", "images/ch4.png", "images/ch5.png",
                     "images/ch6.png", "images/ch7.png", "images/ch8.png"]
            time.sleep(0.1)
            keyboard.type('/')
            time.sleep(0.1)
            keyboard.type('ch')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(0.3)
            mouse.position = (pyautogui.locateCenterOnScreen(cpath[my_thread.n]))
            mouse.press(Button.left)
            mouse.release(Button.left)
            my_thread.n = my_thread.n + 1
        time.sleep(3)
        keyboard.press('a')
        mouse.press(Button.left)
        for i in range(0, 70):
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
        time.sleep(0.1)
        if channel.get() == 1:
            if my_thread.n == 9:
                my_thread.n = 0
            cpath = ["images/ch1.png", "images/ch2.png", "images/ch3.png", "images/ch4.png", "images/ch5.png",
                     "images/ch6.png", "images/ch7.png", "images/ch8.png"]
            time.sleep(0.1)
            keyboard.type('/')
            time.sleep(0.1)
            keyboard.type('ch')
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(0.3)
            mouse.position = (pyautogui.locateCenterOnScreen(cpath[my_thread.n]))
            mouse.press(Button.left)
            mouse.release(Button.left)
            my_thread.n = my_thread.n + 1


class Wrapper:
    def __init__(self):
        self.started = False
        self.n = 1

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
root.title("RapyClicker v0.1.0")
root.resizable(0, 0)
root.call("wm", "attributes", ".", "-topmost", "true")
b1 = ttk.Button(root, text="Start", bootstyle=SUCCESS, command=multi)
b1.pack(side=BOTTOM, padx=10, pady=10)
channel = IntVar()
b2 = ttk.Button(root, text="Stop", bootstyle=(INFO, OUTLINE), command=umulti)
b2.pack(side=BOTTOM, padx=10, pady=10)

label = ttk.Label(text="Podaj czas A:", font=("Calibri", 11), bootstyle="default")
label.pack()
label.place(relx=0.05, rely=0.05)

labela = ttk.Label(text="(Zostaw puste, jeśli chcesz zachować domyślne wartości)", font=("Calibri", 9),
                   bootstyle="default")
labela.pack()
labela.place(relx=0.45, rely=0.06)

entry = ttk.Entry(root)
entry.pack()
entry.place(relx=0.2, rely=0.05)

label2 = ttk.Label(text="Podaj czas B:", font=("Calibri", 11), bootstyle="default")
label2.pack()
label2.place(relx=0.05, rely=0.15)

labela2 = ttk.Label(text="(Zostaw puste, jeśli chcesz zachować domyślne wartości)", font=("Calibri", 9),
                    bootstyle="default")
labela2.pack()
labela2.place(relx=0.45, rely=0.16)

entry2 = ttk.Entry(root)
entry2.pack()
entry2.place(relx=0.2, rely=0.15)

label2 = ttk.Label(text="Zmieniać channel?", font=("Calibri", 11), bootstyle="default")
label2.pack()
label2.place(relx=0.05, rely=0.25)

label3 = ttk.Label(text="Uwaga! Program uruchomi się po 3 sekundach od kliknięcia 'Start'!", font=("Calibri", 11), bootstyle="default")
label3.pack()
label3.place(relx=0.05, rely=0.35)

toggle = ttk.Checkbutton(bootstyle="success-round-toggle", variable=channel, onvalue=1, offvalue=0)
toggle.pack()
toggle.place(relx=0.26, rely=0.26)
root.mainloop()