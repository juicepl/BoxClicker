import tkinter as tk
import pyautogui
import pynput
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time, threading, sys, os
from ctypes import windll
from licensing.models import *
from licensing.methods import Key, Helpers

RSAPubKey = "<RSAKeyValue><Modulus>uxDDH175/MMY611BISqbqrWo+KmcitqIEBPvJbCsvwDDGvyKmzS7Ho9BsqI3FhZ6VA4R5Zan20B7BHCmGQunkDIeTdcPs0RnAnqV1dorz1SMOmeVnus+ury1osTYoSlViDDu1cAH7vyAspXjyxI637vCIWmFhpkIXRHcvs8/ZdowAfLfOpn+qW6COjE2iXzUZnW+mhfzBCaNUYlo6er6rJa/xfsSKLIcweA4GNiIRu9++dx3r0VjDoMFxb6drti0pD+2EDpm7jNrGIdcw6o3ohmP28/fXuymWqnMXuId8DNxrcVMlKwHBc2ACRZPWgeztmFgWmwS4Vg8Iu28liUkIQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyI3NTExMTUzMiIsIkpBcWFpV2poR29XS290M2REZVpHTWsvYXQvTmZxZElFSm1XQzlDNnciXQ=="


def set_appwindow(mainWindow):  # to display the window icon on the taskbar,
    # even when using root.overrideredirect(True
    # Some WindowsOS styles, required for task bar integration
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    # Magic
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)

    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())
def _from_rgb(rgb):
    # translates an rgb tuple of int to a tkinter friendly color code
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


def changex_on_hovering(event):
    global close_button
    close_button['bg'] = "red"


def returnx_to_normalstate(event):
    global close_button
    close_button['bg'] = _from_rgb((112, 68, 196))


def change_size_on_hovering(event):
    global expand_button
    expand_button['bg'] = _from_rgb((15, 3, 33))


def return_size_on_hovering(event):
    global expand_button
    expand_button['bg'] = _from_rgb((112, 68, 196))


def changem_size_on_hovering(event):
    global minimize_button
    minimize_button['bg'] = _from_rgb((15, 3, 33))


def returnm_size_on_hovering(event):
    global minimize_button
    minimize_button['bg'] = _from_rgb((112, 68, 196))


def get_pos(event):  # this is executed when the title bar is clicked to move the window
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx

    def move_window(event):  # runs when window is dragged
        root.config(cursor="fleur")
        root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

    def release_window(event):  # runs when window is released
        root.config(cursor="arrow")

    title_bar.bind('<B1-Motion>', move_window)
    title_bar.bind('<ButtonRelease-1>', release_window)
    title_bar_title.bind('<B1-Motion>', move_window)
    title_bar_title.bind('<ButtonRelease-1>', release_window)

def get_pos2(event):  # this is executed when the title bar is clicked to move the window
    xwin = login.winfo_x()
    ywin = login.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx

    def move_window2(event):  # runs when window is dragged
        login.config(cursor="fleur")
        login.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')

    def release_window2(event):  # runs when window is released
        login.config(cursor="arrow")

    title_bar.bind('<B1-Motion>', move_window2)
    title_bar.bind('<ButtonRelease-1>', release_window2)
    title_bar_title.bind('<B1-Motion>', move_window2)
    title_bar_title.bind('<ButtonRelease-1>', release_window2)


def varlogin():
    licencekeyvar = entryl.get()
    result = Key.activate(token=auth,\
                       rsa_pub_key=RSAPubKey,\
                       product_id=24135, \
                       key=licencekeyvar,\
                       machine_code=Helpers.GetMachineCode(v=2))
    if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
        # an error occurred or the key is invalid or it cannot be activated
        # (eg. the limit of activated devices was achieved)
        labell3 = ttk.Label(login, text="Licencja nie działa:\n {0}".format(result[1]), font=("Calibri", 11), bootstyle="danger")
        labell3.pack()
        labell3.place(relx=0.05, rely=0.6)
    else:

        f2 = open("licence.txt", "a+")
        f2.write(licencekeyvar)
        f2.close()
        # everything went fine if we are here!
        print("Licencja dziala!")
        license_key = result[0]
        print("Licencja konczy sie: " + str(license_key.expires))
        sys.exit(0)

try:
    f = open("licence.txt","r+")
    licencekeyvar = f.read(23)
    f.close()
    print(licencekeyvar)
    result = Key.activate(token=auth, \
                          rsa_pub_key=RSAPubKey, \
                          product_id=24135, \
                          key=licencekeyvar, \
                          machine_code=Helpers.GetMachineCode(v=2))
    if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
        # an error occurred or the key is invalid or it cannot be activated
        # (eg. the limit of activated devices was achieved)
        os.remove("licence.txt")
        sys.exit(0)
    else:
        # everything went fine if we are here!
        print("Licencja dziala!")
        license_key = result[0]
        print("Licencja konczy sie: " + str(license_key.expires))
except FileNotFoundError:
    login_title = "Aktywacja"
    login = ttk.Window(themename="vapor")
    login.geometry('400x250')
    login.title(login_title)
    login.resizable(0, 0)
    login.call("wm", "attributes", ".", "-topmost", "true")
    login.overrideredirect(True)

    login.minimized = False  # only to know if root is minimized
    login.maximized = False  # only to know if root is maximized

    title_bar = tk.Frame(login, relief='raised', bd=0, highlightthickness=0, height=0)
    close_button = tk.Button(title_bar, text='  ×  ', command=login.destroy, padx=2, pady=2, font=("calibri", 13),
                             bd=0, fg='white', highlightthickness=0)
    # minimize_button = tk.Button(title_bar, text=' 🗕 ', command=minimize_me, padx=2, pady=2, bd=0, fg='white',
    #                            font=("calibri", 13), highlightthickness=0)
    title_bar_title = tk.Label(title_bar, text=login_title, bd=0, fg='white', font=("helvetica", 10),
                               highlightthickness=0)

    # a frame for the main area of the window, this is where the actual app will go
    window = tk.Frame(login, highlightthickness=0)

    # pack the widgets
    title_bar.pack(fill=X)
    close_button.pack(side=RIGHT, ipadx=7, ipady=1)
    # minimize_button.pack(side=RIGHT, ipadx=7, ipady=1)
    title_bar_title.pack(side=LEFT, padx=10)
    window.pack(expand=1, fill=BOTH)
    title_bar.bind('<Button-1>', get_pos2)  # so you can drag the window from the title bar
    title_bar_title.bind('<Button-1>', get_pos2)  # so you can drag the window from the title

    # button effects in the title bar when hovering over buttons
    close_button.bind('<Enter>', changex_on_hovering)
    close_button.bind('<Leave>', returnx_to_normalstate)
    entryl = ttk.Entry(login)
    entryl.pack()
    entryl.place(relx=0.3, rely=0.4)

    labell = ttk.Label(login, text="Kod licencji: ", font=("Calibri", 11), bootstyle="default")
    labell.pack(side=TOP)
    labell.place(relx=0.05, rely=0.4)

    labell2 = ttk.Label(login, text="Aktywuj program. ", font=("Calibri", 24), bootstyle="default")
    labell2.pack(side=TOP)
    labell2.place(relx=0.05, rely=0.15)
    bl = ttk.Button(login, text="Kontynuuj", bootstyle=(INFO, OUTLINE), command=varlogin)
    bl.pack(side=BOTTOM, padx=10, pady=10)
    login.mainloop()

if 1==1:
    keyboard = KeyboardController()
    mouse = MouseController()
    event = threading.Event()
    def listener():
        with pynput.keyboard.Listener(
                on_press=on_press) as listener:
            listener.join()
        listener = pynput.keyboard.Listener(
            on_press=on_press)
        listener.start()

    def isFilled(entry):
        try:
            if entry.get() != None and entry.get() != "":
                print(entry.get())
                my_thread.gencount = int(entry.get())
                return True
            else:
                return False
        except TypeError:
            return False
    def program():
        if not isFilled(entryGen):
            umulti()
        print(isFilled(entryGen))
        try:
            my_thread.gen_length = int(entryGenL.get())
            print("input")
        except:
            pass
        try:
            my_thread.gap_length = int(entryGapL.get())
            print("input2")
        except:
            pass
        if not event.is_set():
            time.sleep(3)
            print(channel.get())
            print("works")
            if channel.get() == 1:
                try:
                    keyboard.type('/')
                    time.sleep(0.1)
                    keyboard.type('ch')
                    keyboard.press(pynput.keyboard.Key.enter)
                    keyboard.release(pynput.keyboard.Key.enter)
                    time.sleep(0.3)
                    mouse.position = (pyautogui.locateCenterOnScreen("images/ch1.png"))
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                    time.sleep(2)
                except:
                    keyboard.press(pynput.keyboard.Key.esc)
                    keyboard.release(pynput.keyboard.Key.esc)
            y = 1
            t1 = 0.03
            t2 = 0.16

            isec = int((my_thread.gen_length * 1.3 * my_thread.gencount) + ((my_thread.gencount - 1) * 1.3 * my_thread.gap_length))
            while not event.is_set():
                time.sleep(3)
                keyboard.press('d')
                mouse.press(Button.left)
                for i in range(0, isec):
                    if event.is_set():
                        keyboard.release(pynput.keyboard.Key.shift)
                        mouse.release(Button.left)
                        keyboard.release('d')
                        print("!!!!")
                        sys.exit(0)
                        return
                    keyboard.press(pynput.keyboard.Key.shift)
                    time.sleep(t1)
                    keyboard.release(pynput.keyboard.Key.shift)
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
                    keyboard.press(pynput.keyboard.Key.enter)
                    keyboard.release(pynput.keyboard.Key.enter)
                    time.sleep(0.3)
                    mouse.position = (pyautogui.locateCenterOnScreen(cpath[my_thread.n]))
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                    my_thread.n = my_thread.n + 1
                time.sleep(3)
                keyboard.press('a')
                mouse.press(Button.left)
                for i in range(0, isec):
                    if event.is_set():
                        keyboard.release(pynput.keyboard.Key.shift)
                        mouse.release(Button.left)
                        keyboard.release('a')
                        print("!!!!")
                        sys.exit(0)
                        return
                    keyboard.press(pynput.keyboard.Key.shift)
                    time.sleep(float(t1))
                    keyboard.release(pynput.keyboard.Key.shift)
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
                    keyboard.press(pynput.keyboard.Key.enter)
                    keyboard.release(pynput.keyboard.Key.enter)
                    time.sleep(0.3)
                    mouse.position = (pyautogui.locateCenterOnScreen(cpath[my_thread.n]))
                    mouse.press(Button.left)
                    mouse.release(Button.left)
                    my_thread.n = my_thread.n + 1


    class Wrapper:
        def __init__(self):
            self.started = False
            self.n = 1
            self.gencount = 0
            self.gen_length = 13
            self.gap_length = 9

        def start(self):
            if not self.started:
                self.z = threading.Thread(target=program, daemon=True)
                self.started = True
                self.z.start()

        def stop(self):
            if self.started:
                self.started = False
                self.z = None

    my_thread = Wrapper()


    def on_press(key):
        if format(key) == Key.f5:
            if my_thread.started:
                umulti()
            else:
                multi()


    def multi():
        event.clear()
        my_thread.start()


    def umulti():
        event.set()
        my_thread.stop()
        print("test")


    tk_title = "BoxClicker Beta 2.2"
    root = ttk.Window(themename="vapor")
    root.geometry('600x400')
    root.title(tk_title)
    root.resizable(0, 0)
    root.call("wm", "attributes", ".", "-topmost", "true")
    root.overrideredirect(True)

    root.minimized = False  # only to know if root is minimized
    root.maximized = False  # only to know if root is maximized

    title_bar = tk.Frame(root, relief='raised', bd=0, highlightthickness=0, height=0)





    # put a close button on the title bar
    close_button = tk.Button(title_bar, text='  ×  ', command=root.destroy, padx=2, pady=2, font=("calibri", 13),
                             bd=0, fg='white', highlightthickness=0)
    # minimize_button = tk.Button(title_bar, text=' 🗕 ', command=minimize_me, padx=2, pady=2, bd=0, fg='white',
    #                            font=("calibri", 13), highlightthickness=0)
    title_bar_title = tk.Label(title_bar, text=tk_title, bd=0, fg='white', font=("helvetica", 10),
                               highlightthickness=0)

    # a frame for the main area of the window, this is where the actual app will go
    window = tk.Frame(root, highlightthickness=0)

    # pack the widgets
    title_bar.pack(fill=X)
    close_button.pack(side=RIGHT, ipadx=7, ipady=1)
    # minimize_button.pack(side=RIGHT, ipadx=7, ipady=1)
    title_bar_title.pack(side=LEFT, padx=10)
    window.pack(expand=1, fill=BOTH)  # replace this with your main Canvas/Frame/etc.


    # xwin=None
    # ywin=None
    # bind title bar motion to the move window function


    title_bar.bind('<Button-1>', get_pos)  # so you can drag the window from the title bar
    title_bar_title.bind('<Button-1>', get_pos)  # so you can drag the window from the title

    # button effects in the title bar when hovering over buttons
    close_button.bind('<Enter>', changex_on_hovering)
    close_button.bind('<Leave>', returnx_to_normalstate)

    # some settings
    b1 = ttk.Button(root, text="Start", bootstyle=SUCCESS, command=multi)
    b1.pack(side=BOTTOM, padx=10, pady=10)
    channel = tk.IntVar()
    b2 = ttk.Button(root, text="Stop", bootstyle=(INFO, OUTLINE), command=umulti)
    b2.pack(side=BOTTOM, padx=10, pady=10)

    '''label = ttk.Label(text="Podaj czas A:", font=("Calibri", 11), bootstyle="default")
    label.pack()
    label.place(relx=0.05, rely=0.05)
    
    labela = ttk.Label(text="(Zostaw puste, jeśli chcesz zachować domyślne wartości)", font=("Calibri", 9),
                       bootstyle="default")
    labela.pack()
    labela.place(relx=0.45, rely=0.06)
    
    entry = ttk.Entry(root)
    entry.pack()
    entry.place(relx=0.2, rely=0.05)
    
    labelCh = ttk.Label(text="Podaj czas B:", font=("Calibri", 11), bootstyle="default")
    labelCh.pack()
    labelCh.place(relx=0.05, rely=0.15)
    
    labela2 = ttk.Label(text="(Zostaw puste, jeśli chcesz zachować domyślne wartości)", font=("Calibri", 9),
                        bootstyle="default")
    labela2.pack()
    labela2.place(relx=0.45, rely=0.16)
    
    entry2 = ttk.Entry(root)
    entry2.pack()
    entry2.place(relx=0.2, rely=0.15)'''
    labelX = 0.03
    entryX = 0.5
    labelDX = 0.74
    entryGen = ttk.Entry(root)
    entryGen.pack()
    entryGen.place(relx=entryX, rely=0.15)

    labelGen = ttk.Label(text="Ilość generatorów: ", font=("Calibri", 11), bootstyle="default")
    labelGen.pack()
    labelGen.place(relx=labelX, rely=0.15)

    entryGenL = ttk.Entry(root)
    entryGenL.pack()
    entryGenL.place(relx=entryX, rely=0.25)

    labelGenL = ttk.Label(text="Szerokość generatora: ", font=("Calibri", 11), bootstyle="default")
    labelGenL.pack()
    labelGenL.place(relx=labelX, rely=0.25)

    labelD1 = ttk.Label(text="(Zostaw puste, jeśli chcesz\n zachować domyślne wartości)", font=("Calibri", 8), bootstyle="default")
    labelD1.pack()
    labelD1.place(relx=labelDX, rely=0.25)

    labelGapL = ttk.Label(text="Długość przestrzeni między generatorami: ", font=("Calibri", 11), bootstyle="default")
    labelGapL.pack()
    labelGapL.place(relx=labelX, rely=0.35)

    entryGapL = ttk.Entry(root)
    entryGapL.pack()
    entryGapL.place(relx=entryX, rely=0.35)

    labelD2 = ttk.Label(text="(Zostaw puste, jeśli chcesz\n zachować domyślne wartości)", font=("Calibri", 8), bootstyle="default")
    labelD2.pack()
    labelD2.place(relx=labelDX, rely=0.35)

    labelCh = ttk.Label(text="Zmieniać channel?", font=("Calibri", 11), bootstyle="default")
    labelCh.pack()
    labelCh.place(relx=labelX, rely=0.45)

    toggle = ttk.Checkbutton(bootstyle="success-round-toggle", variable=channel, onvalue=1, offvalue=0)
    toggle.pack()
    toggle.place(relx=0.26, rely=0.46)

    labelInfo = ttk.Label(text="Uwaga! Program uruchomi się po 3 sekundach od kliknięcia 'Start'!", font=("Calibri", 11), bootstyle="default")
    labelInfo.pack()
    labelInfo.place(relx=0.03, rely=0.6)
    root.mainloop()
