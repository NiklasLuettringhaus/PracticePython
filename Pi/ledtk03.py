#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from tkinter import *

GPIO.setmode(GPIO.BCM)
LED = [24,8,7,12]
for i in LED:
    GPIO.setup(i, GPIO.OUT, initial=False)

w = 5
muster = [
    ("Lauflicht nach links",1),
    ("Blinken",2),
    ("Lauflicht nach rechts",3)
    ]

root = Tk()
root.title("Lauflicht")
v = IntVar()
v.set(1)
g = IntVar()
g.set(5)

def LedEin():
    e = v.get()
    t = 1/g.get()
    if e == 1:
        for i in range(w):
            for j in range(4):
                GPIO.output(LED[j], True)
                time.sleep(t)
                GPIO.output(LED[j], False)
    elif e == 2:
        for i in range(w):
            for j in range(4):
                GPIO.output(LED[j], True)
            time.sleep(t)
            for j in range(4):
                GPIO.output(LED[j], False)
            time.sleep(t)
    else:
        for i in range(w):
            for j in range(4):
                GPIO.output(LED[3-j], True)
                time.sleep(t)
                GPIO.output(LED[3-j], False)

Label(root,
      text="Button klicken, um das Lauflicht zu starten").pack()

for txt, m in muster:
    Radiobutton(root,
                text = txt,
                variable = v,
                value = m).pack(anchor=W)

Label(root,
      text="Geschwindigkeit").pack()

Scale(root,
      orient=HORIZONTAL,
      from_ = 1,
      to = 10,
      variable = g).pack()
            
Button(root,
       text="Start",
       command=LedEin).pack(side=LEFT)

root.mainloop()
GPIO.cleanup()
