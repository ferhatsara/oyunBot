import pyautogui
import time
from python_imagesearch import imagesearch
import keyboard
"""
env=(0,0)
a=819
b=358

d = {}
for x in range(1,46):
    if x==6 or x==11 or x==16 or x==21 or x==26 or x==31 or x==36 or x==41:
        a=819
        b=b+38
    d["env{0}".format(x)]=(a,b)
    a=a+39


konum_evet=(452,433)
konum_hayır=(554,434)

def esya_atma(konum1):
    time.sleep(0.2)
    pyautogui.moveTo(901,763)
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
    pyautogui.moveTo(konum1)
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.moveTo(682,524)
    time.sleep(0.2)
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.moveTo(konum_evet)
    time.sleep(1)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()
    time.sleep(0.2)
    pyautogui.moveTo(901,763)
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()

#esya_atma(d["env22"])


"""


def gozetle():
    keyboard.press('q')
    time.sleep(0.1)
    keyboard.send('q')
    

def devriye_at():
    pyautogui.moveTo(506,420)
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(2)
    pyautogui.mouseUp()
    time.sleep(0.2)
    keyboard.press('q')
    time.sleep(4)
    keyboard.send('q')
    pyautogui.mouseDown()
    time.sleep(2)
    pyautogui.mouseUp()
    time.sleep(0.5)
    pyautogui.moveTo(506,566)
    time.sleep(0.2)
    pyautogui.mouseDown()
    time.sleep(2)
    pyautogui.mouseUp()
    time.sleep(0.2)
    keyboard.press('q')
    time.sleep(4)
    keyboard.send('q')
    pyautogui.mouseDown()
    time.sleep(2)
    pyautogui.mouseUp()
    time.sleep(0.5)


def skill():
    hava_kilici= imagesearch.imagesearch('havakilici.PNG')
    if hava_kilici==[-1, -1]:
        keyboard.press('ctrl+h')
        time.sleep(2)
        pyautogui.moveTo(533,759)
        time.sleep(0.3)
        pyautogui.rightClick()
        time.sleep(2)
        keyboard.press('ctrl+g')
    else:
        return




def barones():
    icon=imagesearch.imagesearch('barones.PNG', precision=0.8)
    if icon!=[-1,-1]:
        konum_x=icon[0]
        konum_y=icon[1]+70
        time.sleep(1)
        pyautogui.moveTo(konum_x,konum_y)
        time.sleep(1)
        oluMu=imagesearch.imagesearch('oluq.PNG')
        if oluMu!=[-1,-1]:
            return
        else:
            time.sleep(200)
            barones()
    else:
        return

def azrail():
    icon=imagesearch.imagesearch('azrail.PNG', precision=0.7)
    if icon!=[-1,-1]:
        konum_x=icon[0]
        konum_y=icon[1]+70
        time.sleep(1)
        pyautogui.moveTo(konum_x,konum_y)
        time.sleep(1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        oluMu=imagesearch.imagesearch('oluq.PNG')
        if oluMu!=[-1,-1]:
            return
        else:
            time.sleep(200)
            azrail()
    else:
        return

def azrail2():
    icon=imagesearch.imagesearch('azrail2.PNG', precision=0.8)
    if icon!=[-1,-1]:
        konum_x=icon[0]
        konum_y=icon[1]+70
        time.sleep(1)
        pyautogui.moveTo(konum_x,konum_y)
        time.sleep(1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        oluMu=imagesearch.imagesearch('oluq.PNG')
        if oluMu!=[-1,-1]:
            return
        else:
            time.sleep(200)
            azrail2()
    else:
        return

def ejder():
    icon=imagesearch.imagesearch('ejder.PNG', precision=0.8)
    if icon!=[-1,-1]:
        konum_x=icon[0]
        konum_y=icon[1]+70
        time.sleep(1)
        pyautogui.moveTo(konum_x,konum_y)
        time.sleep(1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        oluMu=imagesearch.imagesearch('oluq.PNG')
        if oluMu!=[-1,-1]:
            return
        else:
            time.sleep(200)
            ejder()
    else:
        return

def kamera_duzelt():
    for i in range(5):
        keyboard.press('f')
    time.sleep(3)
    for i in range(100):
        keyboard.press('g')
    time.sleep(1)
    keyboard.send('g')
    time.sleep(1)
    for i in range(3):
        keyboard.press('t')
    time.sleep(0.5)
    keyboard.send('t')

def metin_kes():
    metin= imagesearch.imagesearch('metin.PNG',precision=0.8)
    if metin!=[-1,-1]:
        metin_x= metin[0]+25
        metin_y= metin[1]+85
        pyautogui.moveTo(metin_x,metin_y)
        time.sleep(1)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(10)
    else:
        return

kamera_sayac=0
while(True):
    #kamera_sayac=kamera_sayac+1
    #if kamera_sayac % 2==0:
        #kamera_duzelt()
    #skill()
    #barones()
    #azrail()
    #azrail2()
    #ejder()
    metin_kes()
    











     

