import pyautogui as pag
import movement as mov
import animatroicChecks as AC

Screen_Dimensions = [0, 0, 640, 480]

def toggleCam():
    pag.moveTo(380, 400)
    pag.moveTo(380, 500, 0.15)
    pag.moveTo(380, 400, 0.1)
    pag.center(Screen_Dimensions)

def toggleMask():
    pag.moveTo(230, 380)
    pag.moveTo(230, 500, 0.1)
    pag.moveTo(230, 380, 0.1)
    pag.center(Screen_Dimensions)
