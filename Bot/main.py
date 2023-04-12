import keyboard
import time
import pyautogui as pag
import movement as mov
import toggles as tog
import animatroicChecks as AC



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
    start = time.time()
    pag.moveTo(268, 371)
    pag.mouseDown(button='left')
    while(time.time() - start > duration and pag.locateOnScreen("Music.jpg",grayscale=True, confidence=.7)):
        time.sleep(.1)
    pag.mouseUp(button="left")
    
def godStrat():
    tog.toggleCam()
    time.sleep(.1)
    AC.TronicInOffice()
    


def autoPlay():
    timeout = 408
    start = time.time()
    pag.leftClick()
    pag.center()
    time.sleep(30)
    mov.lookRight()
    tog.toggleCam() #Cam Up
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
       windMB(10)
       godStrat()
    
while not keyboard.is_pressed('g'):
    if keyboard.is_pressed('c'):
        tog.toggleCam()
    if keyboard.is_pressed('r'):
        AC.rightVent()
    if keyboard.is_pressed('l'):
        AC.leftVent()
    if keyboard.is_pressed('c'):
        windMB()
    if keyboard.is_pressed('m'):
        tog.toggleMask()
    if keyboard.is_pressed('a'):
        autoPlay() #Use when hovering the start button


