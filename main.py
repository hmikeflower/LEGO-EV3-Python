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
t = EV3Brick()


# Write your program here.

#發出 一個聲音
#ev3.speaker.beep()

#改變主機燈光顏色
#t.light.on(Color.YELLOW)

#等待一秒鐘
#wait(1000)

#關閉燈光
#ev3.light.off()

#使用螢幕 screen.draw_text(x, y, text, text_color=Color.BLACK, background_color=None)
#t.screen.draw_text(50, 50, "text", text_color=Color.BLACK, background_color=None)
#wait(5000)

#使用 Touch sensor touch_1 = TouchSensor(Port.S1)
#touch_1 = TouchSensor(Port.S1)
#print(touch_1.pressed())
