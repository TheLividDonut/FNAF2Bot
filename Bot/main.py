import keyboard
import time
import pyautogui as pag
import movement

Test = True

try:
    while Test:
        time.sleep(2)
        x, y = pag.position()
        position = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(position + "\n", end="")
        if keyboard.is_pressed('q'):
            Test = False
except KeyboardInterrupt:
    print("\n")

"""
FNAF 2 Coords
TL: 0, 0
TR: 639, 0
BR: 639, 479
BL: 0, 479
SR = 640x480
"""

direction = 2
#1 = right, 2 = mid, 3 = left

officeTronics = ("GFredInOffice.jpg", "TFredinOffice.jpg", "WBonInOffice.jpg", "WCHicInOffice.png")
TINO = False
#Tronics in Office

def toggleCam():
    pag.moveTo(380, 404)
    pag.moveTo(380, 500, 0.1)
    pag.moveTo(380, 404, 0.1)
    pag.center()

def toggleMask():
    pag.moveTo(150, 426)
    pag.moveTo(150, 458, 0.1)
    pag.moveTo(150, 426, 0.1)
    pag.center()

def shineLight():
    keyboard.press('ctrl')
    time.sleep(.5)

def goToCam11():
    pag.moveTo(590, 286)
    pag.leftClick()

def windMB():
    pag.moveTo(268, 371)
    pag.mouseDown(button='left')

def lookRight():
    global direction
    if(direction == 3):
        movement.sRFL()
    elif(direction == 2):
        movement.sRFM()
    direction = 3

def lookLeft():
    global direction
    if(direction == 2):
        movement.sLFM()
    elif(direction == 1):
        movement.sLFR()
    direction = 1

def leftVent():
    lookLeft()
    pag.moveTo(97, 266)
    pag.mouseDown(button='left')
    time.sleep(.2)
    checkLoc(3)
    
def godStrat():
    global TINO
    toggleCam()
    time.sleep(.1)
    toggleMask()
    if(not TINO):
        toggleMask()
    else:
        while(TINO):
            time.sleep(.1)
        toggleMask()

#Location = 
# 1 = RV 
# 2 = Hall 
# 3 = LV

def checkLoc(location):
    match(location):
        case(1):
            if(pag.locateOnScreen("TBonnie.png", grayscale=True, confidence=.7)):
                pag.mouseUp(button='left')
                toggleMask()
                time.sleep(1)
                while(pag.locateOnScreen("TBMask.jpg", grayscale=True, confidence=.6)):
                    time.sleep(.5)
                toggleMask()
            elif(pag.locateOnScreen("Mangle.png", grayscale=True, confidence=.7)):
                pag.mouseUp(button='left')
                toggleMask()
                time.sleep(5)
                toggleMask()

        case(2):
            if(pag.locateOnScreen("JFoxy.png", grayscale=True, confidence=.7) or pag.locateOnScreen("MFoxy.png", grayscale=True, confidence=.7) or pag.locateOnScreen("BFoxy.png", grayscale=True, confidence=.7)):
                for i in range(6):
                    shineLight()
                    time.sleep(.3)
        case(3):
            if (pag.locateOnScreen("TChica.png", grayscale=True, confidence=.7) or pag.locateOnScreen("BB.png", grayscale=True, confidence=.7)):
                pag.mouseUp(button='left')
                toggleMask()
                time.sleep(5)
                toggleMask()

def TronicInOffice():
    for i in range(4):
        if(pag.locateOnScreen(officeTronics[i], grayscale=True, confidence=.7)):
            toggleMask()
    TINO = True
    while(not pag.locateOnScreen("PostAttackFreddyMask.PNG", grayscale=True, confidence=.9)):
        time.sleep(.1)
    time.sleep(1)
    toggleMask()
    TINO = False