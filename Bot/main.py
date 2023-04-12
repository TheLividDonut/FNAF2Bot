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

def toggleCam():
    pag.moveTo(380, 404)
    pag.moveTo(380, 500, 0.1)
    pag.moveTo(380, 404, 0.1)

def toggleMask():
    pag.moveTo(150, 426)
    pag.moveTo(150, 458, 0.1)
    pag.moveTo(150, 426, 0.1)

def shineLight():
    keyboard.press('ctrl')
    time.sleep(.5)

def goToCam11():
    pag.moveTo(590, 286)
    pag.leftClick()

def windMB():
    pag.moveTo(268, 371)
    pag.mouseDown(button='left')

