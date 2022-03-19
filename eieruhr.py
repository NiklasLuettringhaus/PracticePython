#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from tkinter import *

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

z = [0,0,0,0]
root = Tk()
root.title("Ei")
vm1 = IntVar()
vm1.set(0)
vm2 = IntVar()
vm2.set(0)
vs1 = IntVar()
vs1.set(0)
vs2 = IntVar()
vs2.set(0)

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

def uhr():
  start = time.time()
  zeit = 600 * vm1.get() + 60 * vm2.get() + 10 * vs1.get() + vs2.get() + 1
  ende = start + zeit
  while (zeit > 1):
    zeit = int(ende - time.time())
    m = int(zeit / 60)
    s = zeit % 60
    z[0] = int(m % 100 / 10)
    z[1] = m % 10
    z[2] = int(s / 10)
    z[3] = s % 10
    while int(ende - time.time()) % 60 %10 == z[3]:
      za()
  for s in "abcdef":
    GPIO.output(seg[s], True)
  for i in range(4):
    GPIO.output(ziffer[i], False)

Label(root,
      text="Minuten").grid(row=0,column=0)

Label(root,
      text="Sekunden").grid(row=0,column=2)

Scale(root,
      orient=VERTICAL,
      from_ = 5,
      to = 0,
      variable = vm1).grid(row=1,column=0)

Scale(root,
      orient=VERTICAL,
      from_ = 9,
      to = 0,
      variable = vm2).grid(row=1,column=1)

Scale(root,
      orient=VERTICAL,
      from_ = 5,
      to = 0,
      variable = vs1).grid(row=1,column=2)

Scale(root,
      orient=VERTICAL,
      from_ = 9,
      to = 0,
      variable = vs2).grid(row=1,column=3)

Button(root,
       text="Start",
       command=uhr).grid(row=6,column=0)

root.mainloop()
GPIO.cleanup()
