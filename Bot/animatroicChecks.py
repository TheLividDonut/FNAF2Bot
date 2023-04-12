import keyboard
import time
import pyautogui as pag
import toggles as tog
import movement as mov

TINO = False
officeTronics = ("GFredInOffice.jpg", "TFredinOffice.jpg", "WBonInOffice.jpg", "WCHicInOffice.png")

def getTINO():
    return TINO

def leftVent():
    mov.lookLeft()
    pag.moveTo(97, 266)
    pag.mouseDown(button='left')
    time.sleep(.2)
    checkLoc(3)

def rightVent():
    mov.lookRight()
    pag.moveTo(546, 266)
    pag.mouseDown(button='left')
    time.sleep(.2)
    checkLoc(1)

def hallWay():
    mov.lookMid()
    keyboard.press('ctrl')
    time.sleep(.5)
    checkLoc(2)
    keyboard.release('ctrl')


#Location = 
# 1 = RV 
# 2 = Hall 
# 3 = LV

def checkLoc(location):
    match(location):
        case(1):
            if(pag.locateOnScreen("TBonnie.png", grayscale=True, confidence=.7)):
                pag.mouseUp(button='left')
                tog.toggleMask()
                time.sleep(1)
                while(pag.locateOnScreen("TBMask.jpg", grayscale=True, confidence=.6)):
                    time.sleep(.5)
                tog.toggleMask()
            elif(pag.locateOnScreen("Mangle.png", grayscale=True, confidence=.7)):
                pag.mouseUp(button='left')
                tog.toggleMask()
                time.sleep(5)
                tog.toggleMask()
            else:
                pag.mouseUp(button='left')

        case(2):
            if(pag.locateOnScreen("JFoxy.png", grayscale=True, confidence=.7) or pag.locateOnScreen("MFoxy.png", grayscale=True, confidence=.7) or pag.locateOnScreen("BFoxy.png", grayscale=True, confidence=.7)):
                for i in range(6):
                    tog.shineLight()
                    time.sleep(.3)
        case(3):
            if (pag.locateOnScreen("TChica.png", grayscale=True, confidence=.7) or pag.locateOnScreen("BB.png", grayscale=True, confidence=.7)):
                pag.mouseUp(button='left')
                tog.toggleMask()
                time.sleep(5)
                tog.toggleMask()
            else:
                pag.mouseUp(button='left')

def TronicIOTest():
    global TINO
    for i in range(4):
        if(pag.locateOnScreen(officeTronics[i], grayscale=True, confidence=.7)):
            TINO = True
            return True
        else:
            TINO = False
            return False

def TronicInOffice():
    global TINO
    if(TronicIOTest):
        tog.toggleMask()
        while(not pag.locateOnScreen("PostAttackFreddyMask.PNG", grayscale=True, confidence=.9)):
            time.sleep(.1)
        time.sleep(1)
        tog.toggleMask()
        TINO = False    