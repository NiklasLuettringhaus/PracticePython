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

z = [0,0,0,0]
print("Strg+C beendet das Programm")

def za():
    for i in range(4):
      for s in "abcdefg":
        GPIO.output(seg[s], False)
      GPIO.output(ziffer[i], False)
      for s in zahl[z[i]]:
        GPIO.output(seg[s], True)
      time.sleep(0.001)
      GPIO.output(ziffer[i], True)

try:
  while True:
    s = input("Bitte vierstellige Zahl eingeben:")
    s += "0000"
    for i in range(4):
      if s[i].isdigit():
        z[i] = int(s[i])
      else:
        z[i] = 0
    sek = time.time()
    while time.time() <= sek + 2:
      za()

except KeyboardInterrupt:
  GPIO.cleanup()
