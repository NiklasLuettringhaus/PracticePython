#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED = [23,8,12,21]
for i in LED:
    GPIO.setup(i, GPIO.OUT, initial=False)

TAST = [18,7,20,16]
for i in TAST:
    GPIO.setup(i, GPIO.IN, GPIO.PUD_DOWN)

TON = 4
GPIO.setup(TON, GPIO.OUT)
freq = [494,440,370,294]

def LEDein(n, z):
    piep = GPIO.PWM(TON, freq[n])
    piep.start(1)
    GPIO.output(LED[n], True)
    time.sleep(z)
    GPIO.output(LED[n], False)
    piep.stop()
    time.sleep(0.15)
 
def Druecken():
    while True:
        if(GPIO.input(TAST[0])):
            return 0
        if(GPIO.input(TAST[1])):
            return 1
        if(GPIO.input(TAST[2])):
            return 2
        if(GPIO.input(TAST[3])):
            return 3

print("Strg+C beendet das Programm")

try:
    while True:
        taste = Druecken()
        LEDein(taste, 0.2)

except KeyboardInterrupt:
    for j in range(4):
        GPIO.output(LED[j], True)
    time.sleep(0.05)
    for j in range(4):
        GPIO.output(LED[j], False)
    GPIO.cleanup()
