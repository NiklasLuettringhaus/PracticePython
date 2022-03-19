#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os

g1 = 10; g2 = 100; g3 = 500; g4 = 1000

GPIO.setmode(GPIO.BCM)
LED = [8,7,12]
for i in range(3):
  GPIO.setup(LED[i], GPIO.OUT, initial=False)

print("Strg+C beendet das Programm")

try:
  while True :
    s = os.statvfs('/')
    f = s.f_bsize * s.f_bavail / 1048576

    if f < g1:
      x = "100"
    elif f < g2:
      x = "110"
    elif f < g3:
      x = "010"
    elif f < g4:
      x = "011"
    else:
      x = "001"

    for i in range(3):
      GPIO.output(LED[i], int(x[i]))
    time.sleep(1.0)

except KeyboardInterrupt:
  GPIO.cleanup()
