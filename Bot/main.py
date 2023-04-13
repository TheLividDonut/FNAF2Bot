import keyboard
import time
import pyautogui as pag
import movement as mov
import toggles as tog
import animatroicChecks as AC
import cv2

#Images
GreyMB= cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\GreyMB.png")
GreenMB = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\Music.png")

"""
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
#Stuff to get mouse position

"""
FNAF 2 Coords
TL: 0, 0
TR: 639, 0
BR: 639, 479
BL: 0, 479
SR = 640x480
"""

def goToCam11():
    pag.moveTo(590, 286)
    pag.leftClick()
#Only useful at the start of the night

def windMB(duration):
    Winding = pag.locateOnScreen(GreenMB,grayscale=True, confidence=.5) is not None
    NotWinding = pag.locateOnScreen(GreyMB,grayscale=True, confidence=.7) is not None
    start = time.time()
    pag.moveTo(268, 371)
    pag.mouseDown(button='left')
    print(Winding)
    print(NotWinding)
    while(time.time() - start < duration):# and (Winding or NotWinding)):
        pag.mouseDown(button='left')
    pag.mouseUp(button="left")
    
def godStrat():
    tog.toggleCam()
    time.sleep(.1)
    AC.OfficeCheck() 

def autoPlay():
    timeout = 408
    start = time.time()
    pag.leftClick()
    pag.center()
    time.sleep(30)
    mov.lookRight()
    tog.toggleCam() #Cam Ups
    goToCam11()
    windMB(20)
    godStrat() #Cam Down
    pag.center()
    while(time.time() - start > timeout):
       AC.rightVent()
       AC.hallWay()
       AC.leftVent()
       AC.hallWay()
       AC.rightVent()
       tog.toggleCam() #Cam up\
       windMB(3)
       godStrat()
    
while not keyboard.is_pressed('g'):
    if keyboard.is_pressed('c'):
        tog.toggleCam()
    if keyboard.is_pressed('r'):
        AC.rightVent()
    if keyboard.is_pressed('l'):
        AC.leftVent()
    if keyboard.is_pressed('s'):
        windMB(5)
    if keyboard.is_pressed('m'):
        tog.toggleMask()
    if keyboard.is_pressed('a'):
        autoPlay() #Use when hovering the start button
    if keyboard.is_pressed('f'):
        godStrat()
        


