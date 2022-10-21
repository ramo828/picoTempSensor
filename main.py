from machine import Pin, I2C
import utime
import os
from mylib import ferq,smoothData, ln, calc, calcTemp
from ssd1306 import SSD1306_I2C
import math


analog_value = machine.ADC(28)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=200000)   # Init I2C using pins
oled = SSD1306_I2C(128, 64, i2c, addr=0x3c)   # Init oled display
count = 1


while True:
    external = analog_value.read_u16()
    internal = sensor_temp.read_u16()     
    internalData = internal*conversion_factor
    externalData = external*conversion_factor
    temperature = 27 - (internalData - 0.706)/0.001721
    print("Real: ",calc(external),smoothData(calc(external)))
    temperature1= calcTemp(smoothData(calc(external)))- 3
    ferqData = ferq(calcTemp(smoothData(calc(external)))- 3,temperature)
    print(temperature1)
    print(temperature)
    print("Fərq: ",ferqData)
    oled.fill(0)
    oled.text("Internal: "+str(temperature),0,0)
    oled.text("External: "+str(temperature1),0,20)
    oled.text("Ferqler: "+str(ferqData),0,40)
    oled.hline(0, 50, 128, 5)               # draw horizontal line x=0, y=8, width=4, colour=1
    oled.hline(0, 10, 128, 5)               # draw horizontal line x=0, y=8, width=4, colour=1
    oled.hline(0, 30, 128, 5)               # draw horizontal line x=0, y=8, width=4, colour=1
    if(count> 128):
        count = 1
    oled.hline(count, 60, count, 5)               # draw horizontal line x=0, y=8, width=4, colour=1

    oled.show()
    print(count)
    count*=2
    