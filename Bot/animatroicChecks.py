import keyboard
import time
import pyautogui as pag
import toggles as tog
import movement as mov

officeTronics = ("GFredInOffice.png", "TFredinOffice.png", "WBonInOffice.png", "WCHicInOffice.png")

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
            Tbonnie = pag.locateOnScreen("TBonnie.png", grayscale=True, confidence=.7) is not None
            Mangle = pag.locateOnScreen("Mangle.png", grayscale=True, confidence=.7) is not None
            if(Tbonnie):
                pag.mouseUp(button='left')
                tog.toggleMask()
                time.sleep(1)
                endAttack = pag.locateOnScreen("TBMask.png", grayscale=True, confidence=.6) is not None
                while(not endAttack):
                    time.sleep(.5)
                tog.toggleMask()
            elif(Mangle):
                pag.mouseUp(button='left')
                tog.toggleMask()
                time.sleep(5)
                tog.toggleMask()
            else:
                pag.mouseUp(button='left')

        case(2):
            JustFoxy = pag.locateOnScreen("JFoxy.png", grayscale=True, confidence=.7) is not None
            MangleFoxy = pag.locateOnScreen("MFoxy.png", grayscale=True, confidence=.7) is not None
            BonnieFoxy = pag.locateOnScreen("BFoxy.png", grayscale=True, confidence=.7) is not None
            FoxyCheck = (JustFoxy or MangleFoxy or BonnieFoxy)
            if(FoxyCheck):
                for i in range(6):
                    tog.shineLight()
                    time.sleep(.3)
        case(3):
            TChica = pag.locateOnScreen("TChica.png", grayscale=True, confidence=.7) is not None
            BB = pag.locateOnScreen("TChica.png", grayscale=True, confidence=.7) is not None
            if (TChica or BB):
                pag.mouseUp(button='left')
                tog.toggleMask()
                time.sleep(5)
                tog.toggleMask()
            else:
                pag.mouseUp(button='left')

def TronicIOTest():
    for i in range(4):
        TronicInOffice = pag.locateOnScreen(officeTronics[i], grayscale=True, confidence=.7) is not None
        if(TronicInOffice):
            return True
        else:
            return False

def OfficeCheck():
    if(TronicIOTest):
        tog.toggleMask()
        while(not pag.locateOnScreen("PostAttackFreddyMask.PNG", grayscale=True, confidence=.9)):
            time.sleep(.1)
        time.sleep(1)
        tog.toggleMask()   