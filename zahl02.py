#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

seg={'a':12, 'b':7, 'c':18, 'd':21, 'e':20, 'f':8, 'g':16}
for s in "abcdefg":
  GPIO.setup(seg[s], GPIO.OUT, initial=False)

ziffer=[25, 24, 23, 4]
for z in ziffer:
  GPIO.setup(z, GPIO.OUT, initial=False)

zahl=[
  "abcdef",  #0
  "bc",      #1
  "abdeg",   #2
  "abcdg",   #3
  "bcfg",    #4
  "acdfg",   #5
  "acdefg",  #6
  "abc",     #7
  "abcdefg", #8
  "abcdfg",  #9
    ]

print("Strg+C beendet das Programm")
try:
  while True:
    for i in range(4):
      for s in "abcdefg":
        GPIO.output(seg[s], False)
      GPIO.output(ziffer[i], False)
      for s in zahl[i+1]:
        GPIO.output(seg[s], True)
      time.sleep(0.001)
      GPIO.output(ziffer[i], True)

except KeyboardInterrupt:
  GPIO.cleanup()
