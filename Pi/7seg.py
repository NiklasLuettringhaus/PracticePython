#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

seg=[12, 7, 18, 21, 20, 8, 16, 27]
for s in seg:
  GPIO.setup(s, GPIO.OUT, initial=False)

ziffer=[25, 24, 23, 4]
for z in ziffer:
  GPIO.setup(z, GPIO.OUT, initial=True)

print("Strg+C beendet das Programm")
try:
  while True:
    for z in range(4):
      GPIO.output(ziffer[z], False)
      for s in range(8):
        GPIO.output(seg[s], True)
        time.sleep(0.1)
      for s in range(8):
        GPIO.output(seg[s], False)
        time.sleep(0.1)
      GPIO.output(ziffer[z], True)

except KeyboardInterrupt:
  GPIO.cleanup()
