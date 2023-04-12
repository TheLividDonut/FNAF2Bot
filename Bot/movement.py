import keyboard
import time
import pyautogui as pag

direction = 2
#1 = right, 2 = mid, 3 = left

def sRFM():
    pag.moveTo(0, 240)
    time.sleep(.5)
    pag.moveTo(320, 240)

def sRFL():
    pag.moveTo(0, 240)
    time.sleep(1)
    pag.moveTo(320, 240)

def sLFM():
    pag.moveTo(639, 240)
    time.sleep(.5)
    pag.moveTo(320, 240)

def sLFR():
    pag.moveTo(639, 240)
    time.sleep(1)
    pag.moveTo(320, 240)

def sMFL():
    pag.moveTo(0, 240)
    time.sleep(.5)
    pag.moveTo(320, 240)

def sMFR():
    pag.moveTo(639, 240)
    time.sleep(.5)
    pag.moveTo(320, 240)

def lookRight():
    global direction
    if(direction == 3):
        sRFL()
    elif(direction == 2):
        sRFM()
    direction = 3

def lookLeft():
    global direction
    if(direction == 2):
        sLFM()
    elif(direction == 1):
        sLFR()
    direction = 1

def lookMid():
    global direction
    if(direction == 1):
        sMFR()
    elif(direction == 3):
        sMFL()
    direction = 2

def getDirection():
    return direction