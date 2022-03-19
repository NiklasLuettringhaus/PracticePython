#!/usr/bin/python
import RPi.GPIO as GPIO
import time, os

GPIO.setmode(GPIO.BCM)

seg={'a':12, 'b':7, 'c':18, 'd':21, 'e':20, 'f':8, 'g':16}
for s in "abcdefg":
  GPIO.setup(seg[s], GPIO.OUT, initial=False)

ziffer=[25, 24, 23, 4]
for z in ziffer:
  GPIO.setup(z, GPIO.OUT, initial=True)

dp = 27
GPIO.setup(dp, GPIO.OUT, initial=False)

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

z = [0,0,0]
ip = os.popen("hostname -I").readline()[:-2].split(".")

print("Strg+C beendet das Programm")

def za():
    for i in range(3):
      for s in "abcdefg":
        GPIO.output(seg[s], False)
      GPIO.output(ziffer[i], False)
      for s in zahl[z[i]]:
        GPIO.output(seg[s], True)
      time.sleep(0.001)
      GPIO.output(ziffer[i], True)

def blink():
    for s in "abcdefg":
      GPIO.output(seg[s], False)
    for k in range(3):
      GPIO.output(ziffer[k], False)
    GPIO.output(dp, True)
    time.sleep(0.5)
    GPIO.output(dp, False)  

try:
  while True:
    for j in ip:
      for k in range(3):
        z[k] = int(j.rjust(3, "0")[k])
      sek = time.time()
      while time.time() <= sek + 1:
        za()
    blink()

except KeyboardInterrupt:
  GPIO.cleanup()
