#!/usr/bin/python
import RPi.GPIO as GPIO
import time, random
from tkinter import *

GPIO.setmode(GPIO.BCM)
seg={'a':12, 'b':7, 'c':18, 'd':21, 'e':20, 'f':8, 'g':16}
for s in "abcdefg":
  GPIO.setup(seg[s], GPIO.OUT, initial=False)

ziffer=[25, 24, 23, 4]
for z in ziffer:
  GPIO.setup(z, GPIO.OUT, initial=True)

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
  "abcdef",  #10
  "bcef",    #11
  "bcefg",   #12
    ]

wz = [
    ("1 Würfel",1),
    ("2 Würfel",2),
    ("3 Würfel",3),
    ("4 Würfel",4)
    ]

wa = [
    ("W4 - Tetraeder",4,1),
    ("W6 - Würfel",6,2),
    ("W8 - Oktaeder",8,3),
    ("W12 - Dodekaeder",12,4)
    ]

root = Tk()
root.title("Würfel")
vz = IntVar()
vz.set(4)
va = IntVar()
va.set(6)
vd = IntVar()
vd.set(5)

def wurf():
    z = [0,0,0,0]
    ez = vz.get()
    ea = va.get()
    ed = vd.get()
    for i in range(ez):
        z[i] = random.randrange(1, ea + 1)
    sek = time.time()
    while time.time() <= sek + ed:
        for i in range(ez):
          for s in "abcdefg":
            GPIO.output(seg[s], False)
          GPIO.output(ziffer[i], False)
          for s in zahl[z[i]]:
            GPIO.output(seg[s], True)
          time.sleep(0.001)
          GPIO.output(ziffer[i], True)

Label(root,
      text="Zahl der Würfel").grid(row=0,column=0)

for txt, n in wz:
    Radiobutton(root,
                text = txt,
                variable = vz,
                value = n).grid(row=n,column=0,sticky=W)
Label(root,
      text="Art der Würfel").grid(row=0,column=1)

for txt, a, n in wa:
    Radiobutton(root,
                text = txt,
                variable = va,
                value = a).grid(row=n,column=1,sticky=W)

Label(root,
      text="Dauer (Sekunden)").grid(row=5,column=1)
            
Scale(root,
      orient=HORIZONTAL,
      from_ = 1,
      to = 10,
      variable = vd).grid(row=6,column=1)

Button(root,
       text="Würfeln",
       command=wurf).grid(row=6,column=0)

root.mainloop()
GPIO.cleanup()
