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

z = [0,0,0,0]
print("Strg+C beendet das Programm")

def za():
    for i in range(4):
      for s in "abcdefg":
        GPIO.output(seg[s], False)
      GPIO.output(ziffer[i], False)
      for s in zahl[z[i]]:
        GPIO.output(seg[s], True)
      if i == 1:
        GPIO.output(dp, True)
      else:
        GPIO.output(dp, False)        
      time.sleep(0.001)
      GPIO.output(ziffer[i], True)

try:
  while True:
    zeit = time.localtime()
    h = zeit.tm_hour
    m = zeit.tm_min
    z[0] = int(h / 10)
    z[1] = h % 10
    z[2] = int(m / 10)
    z[3] = m % 10
    while time.localtime().tm_min == m:
      za()

except KeyboardInterrupt:
  GPIO.cleanup()
