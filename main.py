import machine
import utime
import os
from mylib import ferq,smoothData, ln, calc, calcTemp

analog_value = machine.ADC(28)
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = analog_value.read_u16()
    reading1 = sensor_temp.read_u16()     
    read1 = reading1*conversion_factor
    read = reading*conversion_factor
    temperature1 = 27 - (read1 - 0.706)/0.001721
    print("Real: ",calc(reading),smoothData(calc(reading)))
    print(calcTemp(smoothData(calc(reading)))- 3)
    print(temperature1)
    print("Fərq: ",ferq(calcTemp(smoothData(calc(reading)))- 3,temperature1))

    