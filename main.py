import machine
import utime
import os
from mylib import ferq,smoothData, ln, calc, calcTemp

analog_value = machine.ADC(28)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    external = analog_value.read_u16()
    internal = sensor_temp.read_u16()     
    internalData = internal*conversion_factor
    externalData = external*conversion_factor
    temperature = 27 - (internalData - 0.706)/0.001721
    print("Real: ",calc(external),smoothData(calc(external)))
    print(calcTemp(smoothData(calc(external)))- 3)
    print(temperature)
    print("Fərq: ",ferq(calcTemp(smoothData(calc(external)))- 3,temperature))

    