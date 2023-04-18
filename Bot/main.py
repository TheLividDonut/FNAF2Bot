import keyboard
import time
import pyautogui as pag
import movement as mov
import toggles as tog
import animatroicChecks as AC
import cv2

#Images
GreyMB= cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\GreyMB.png")
GreenMB = cv2.imread(r"C:\Users\Noah\Desktop\Computer Stuff\Programming\FNAF2 Bot Stuff\GreenMB2.png")

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

def returnMB():
    Winding = pag.locateOnScreen(GreenMB,grayscale=False, confidence=.6) is not None
    NotWinding = pag.locateOnScreen(GreyMB,grayscale=False, confidence=.9) is not None
    print(NotWinding)
    print(Winding)

def windMB(duration):
    Winding = pag.locateOnScreen(GreenMB,grayscale=False, confidence=.6) is not None
    NotWinding = pag.locateOnScreen(GreyMB,grayscale=False, confidence=.9)
    start = time.time()
    loopStart = start
    integral = 1
    onScreen = False
    pag.moveTo(NotWinding)
    pag.mouseDown(button='left')
    if(Winding):
        #If the music box is winding
        onScreen = True
        #Green box on screen
        while(onScreen):
            #While it is on screen
            if(time.time() - start < duration and time.time() - loopStart >= integral):
                #checks if 
                if(not Winding):
                    time.sleep(.1)
                    if(not Winding):
                        onScreen = False
                loopStart = time.time()
                #resets loopStart value to new interval
    pag.mouseUp(button='left')
    if(time.time() - start < duration):
        #Checks if the camera was pulled down premptively
        time.sleep(.2)
        tog.toggleMask()
        AC.OfficeCheck()
    else:
        godStrat()

def godStrat():
    tog.toggleCam()
    time.sleep(.1)
    AC.OfficeCheck()

def autoPlay():
    timeout = 408
    start = time.time()
    pag.leftClick()
    pag.moveTo(320, 240)
    time.sleep(30)
    mov.lookRight()
    tog.toggleCam() #Cam Ups
    goToCam11()
    windMB(20) #Cam Down
    while(time.time() - start > timeout):
       AC.rightVent()
       AC.hallWay()
       AC.leftVent()
       AC.hallWay()
       AC.rightVent()
       tog.toggleCam() #Cam up\
       windMB(3)
    
while not keyboard.is_pressed('g'):
    if keyboard.is_pressed('c'):
        tog.toggleCam()
    if keyboard.is_pressed('r'):
        AC.rightVent()
    if keyboard.is_pressed('l'):
        AC.leftVent()
    if keyboard.is_pressed('s'):
        #pag.mouseDown(button='left')
        windMB(5)
    if keyboard.is_pressed('m'):
        tog.toggleMask()
    if keyboard.is_pressed('a'):
        autoPlay() #Use when hovering the start button
    if keyboard.is_pressed('f'):
        godStrat()
    if keyboard.is_pressed('v'):
        returnMB()
        