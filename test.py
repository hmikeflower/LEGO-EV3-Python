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


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
#發出 一個聲音
#ev3.speaker.beep()

#改變主機燈光顏色
#ev3.light.on(Color.RED)

#等待一秒鐘
#wait(1000)

#關閉燈光
#ev3.light.off()

#使用螢幕
#ev3.screen.clear()
#ev3.screen.draw_text(50, 59, "123", text_color=Color.BLACK, background_color=None)

#使用touch 先建立一個變數來控制 touch
#指定 port
touch_1 = TouchSensor(Port.S1)
touch_4 = TouchSensor(Port.S4)
print(touch_1.pressed())
def show(a,x,y):
    
    ev3.screen.draw_text(x, y, a, text_color=Color.BLACK, background_color=None)

t1=0
t2=0
while True :
    if touch_1.pressed() == True:
            t1+=1
    ev3.screen.clear()
    show(t1,50,50)
    show(t2,100,100)    
    wait(100)