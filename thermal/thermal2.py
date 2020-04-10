import serial, time
import datetime as dt
import numpy as np
import cv2

#### max and min val Temp
Tmax = 40
Tmin = 20
sp = 'ttyUSB0'
br = 9600  # Baud
buffer=768
print('opening Serial port /dev/' + sp + ' Baud=' + str(br))
try:
    ser = serial.Serial('/dev/' + sp)
    ser.baudrate = br
except:
    print('failed to open port // maybe permission issue')
    exit(1)



