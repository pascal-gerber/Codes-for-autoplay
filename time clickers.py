from tkinter import *
import keyboard
import time
import random
import threading
import mouse

upgrader = None
upgradertoggle = False
abilitytoggle = False
clickertoggle = False
Zerotoggle = False

def listenforF2():
    while 1:
        keyboard.wait("F2")
        threadcommand(autoclicker)

def threadcommand(functions):
    launched = threading.Thread(target=functions)
    launched.start()
    

def autoupgrades():
    global upgrader
    global upgradertoggle
    upgradertoggle = not upgradertoggle
    
    items = ["a", "s", "d", "f", "g"]
    while 1:
        if upgradertoggle == True:
            upgrader.configure(bg = "Green")
            keyboard.press_and_release(random.choice(items))
            time.sleep(3)
        else:
            upgrader.configure(bg = "Red")
            break
            

def autoability():
    global ability
    global abilitytoggle
    abilitytoggle = not abilitytoggle
    while 1:
        if abilitytoggle == True:
            ability.configure(bg = "Green")
            keyboard.press_and_release("space")
            time.sleep(60)
        else:
            ability.configure(bg = "Red")
            break

def autoclicker():
    global clicker
    global clickertoggle
    clickertoggle = not clickertoggle
    while 1:
        if clickertoggle == True:
            clicker.configure(bg = "Green")
            mouse.click("left")
            time.sleep(0.1)
        else:
            clicker.configure(bg = "Red")
            break

def autoZero():
    global Zero
    global Zerotoggle
    Zerotoggle = not Zerotoggle
    while 1:
        if Zerotoggle == True:
            Zero.configure(bg = "Green")
            keyboard.press_and_release("0")
            time.sleep(3601)
        else:
            Zero.configure(bg = "Red")
            break
        

def makewindow():
    global upgrader
    global ability
    global clicker
    global Zero

    listen = threading.Thread(target = listenforF2)
    listen.start()
    
    window = Tk()

    upgrader = Button(text="Autoupgrader", height = 5, width = 20,
                      command=lambda autoupgrades = autoupgrades: threadcommand(autoupgrades), bg = "Red")
    upgrader.grid(row = 0, column = 0)

    ability = Button(text="Ability", height = 5, width = 20,
                     command=lambda autoability = autoability: threadcommand(autoability), bg = "Red")
    ability.grid(row = 0, column = 1)

    clicker = Button(text="Autoclicker (press F2)", height = 5, width = 20,
                     command=lambda autoclicker = autoclicker: threadcommand(autoclicker), bg = "Red")
    clicker.grid(row = 1, column = 0)

    Zero = Button(text="Zero", height = 5, width = 20,
                     command=lambda autoZero = autoZero: threadcommand(autoZero), bg = "Red")
    Zero.grid(row = 1, column = 1)
    
    window.title("time clicker autoplayer")
    window.geometry("500x500")
    window.mainloop()

makewindow()
