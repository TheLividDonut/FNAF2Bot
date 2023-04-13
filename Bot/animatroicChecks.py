import keyboard
import time
import pyautogui as pag
import toggles as tog
import movement as mov
import cv2

BB = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\BB.png")
BF = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\BFoxy.png")
GFH = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\GFredInHallway.png")
GFO= cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\GFredInOffice.png")
JF = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\JFoxy.png")
M = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\Mangle.png")
MF = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\MFoxy.png")
PAFM = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\PostAttackFreddyMask.png")
TBM = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\TBMask.png")
TB = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\TBonnie.png")
TC = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\TChica.png")
TF = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\TFredinOffice.png")
WB = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\WBonInOffice.png")
WC = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\WChicInOffice.png")

officeTronics = (GFO, TF, WB, WC)

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
            Tbonnie = pag.locateOnScreen(TB, grayscale=True, confidence=.7) is not None
            Mangle = pag.locateOnScreen(M, grayscale=True, confidence=.7) is not None
            if(Tbonnie):
                pag.mouseUp(button='left')
                tog.toggleMask()
                time.sleep(1)
                endAttack = pag.locateOnScreen(TBM, grayscale=True, confidence=.6) is not None
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
            JustFoxy = pag.locateOnScreen(JF, grayscale=True, confidence=.7) is not None
            MangleFoxy = pag.locateOnScreen(MF, grayscale=True, confidence=.7) is not None
            BonnieFoxy = pag.locateOnScreen(BF, grayscale=True, confidence=.7) is not None
            FoxyCheck = (JustFoxy or MangleFoxy or BonnieFoxy)
            if(FoxyCheck):
                for i in range(6):
                    tog.shineLight()
                    time.sleep(.3)
        case(3):
            TChica = pag.locateOnScreen(TC, grayscale=True, confidence=.7) is not None
            BB = pag.locateOnScreen(BB, grayscale=True, confidence=.7) is not None
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
        while(pag.locateOnScreen(PAFM, grayscale=True, confidence=.9) is not None):
            time.sleep(.1)
        time.sleep(1)
        tog.toggleMask()   