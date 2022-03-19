#!/usr/bin/python
import RPi.GPIO as GPIO
from tkinter import *

LED = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

def LedEin():
    GPIO.output(LED,True)
    
def LedAus():
    GPIO.output(LED,False)

root = Tk()
root.title("LED")
Label(root,
      text="Button klicken, um die LED ein- oder auszuschalten").pack()

Button(root,
       text="Ein",
       command=LedEin).pack(side=LEFT)

Button(root,
       text="Aus",
       command=LedAus).pack(side=LEFT)

root.mainloop()

GPIO.cleanup()
