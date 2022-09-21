#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
# 使用 LEGO EV3 PYTHON 使用兩個觸控 比誰按得快，先按10下的獲勝

# Create your objects here.
ev3 = EV3Brick()
ev3.speaker.beep()

#使用touch 先建立一個變數來控制 touch
#指定 port
touch_1 = TouchSensor(Port.S1)
touch_4 = TouchSensor(Port.S4)



def ShowWithText(a,b,x,y):
    ev3.screen.draw_text(x, y,a+str(b), text_color=Color.BLACK, background_color=None)

def Show(a,x,y):
    ev3.screen.draw_text(x, y,a, text_color=Color.BLACK, background_color=None)

t1=0
t4=0
mode=True

TP1=True
TP4=True

while mode :
    
    if touch_1.pressed() == True: #41~45行 避免 觸控連點
        TP1=False
    elif touch_1.pressed() == False and TP1==False:
        TP1=True
        t1+=1
    
    if touch_4.pressed() == True:
        TP4=False
    elif touch_4.pressed() == False and TP4==False:
        TP4=True
        t4+=1
    if t1> 9 or t4>9:
        mode = False
    ev3.screen.clear()
    ShowWithText("Touch1:",t1,50,50)
    ShowWithText("Touch4:",t4,50,100)    
    wait(50)

ev3.screen.clear()
Show("Wait a moment",10,50)
wait(2000)

if t1==t4:
    ev3.screen.clear()
    Show("This game ended in a tie",10,50)
elif t1>t4:
    ev3.screen.clear()
    Show("T1 WIN",10,50)
elif t4>t1:
    ev3.screen.clear()
    Show("T4 WIN",10,50)