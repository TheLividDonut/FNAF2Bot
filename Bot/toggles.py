import keyboard
import time
import pyautogui as pag
import movement as mov
import animatroicChecks as AC

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
