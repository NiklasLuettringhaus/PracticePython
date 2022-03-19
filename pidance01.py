#!/usr/bin/python
import time, random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED = [23,8,12,21]
for i in LED:
    GPIO.setup(i, GPIO.OUT, initial=False)

TAST = [18,7,20,16]
for i in TAST:
    GPIO.setup(i, GPIO.IN, GPIO.PUD_DOWN)

def LEDein(n, z):
    GPIO.output(LED[n], True)
    time.sleep(z)
    GPIO.output(LED[n], False)
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

rzahl = 10
farbe = []
for i in range(rzahl):
    farbe.append(random.randrange(4))
ok = True

for runde in range(1, rzahl +1):
    print("Runde", runde)
    for i in range(runde):
        LEDein(farbe[i], 1)
    for i in range(runde):
        taste = Druecken()
        LEDein(taste, 0.2)
        if(taste != farbe[i]):
            print("Verloren!")
            print("Du hast es bis Runde", runde - 1, "geschafft")
            for j in range(4):
                GPIO.output(LED[j], True)
            for j in range(4):
                time.sleep(0.5)
                GPIO.output(LED[j], False)
            ok = False
            break
    if(ok == False):
        break
    time.sleep(0.5)

if(ok == True):
    print("Super gemacht!")
    for i in range(5):
        for j in range(4):
            GPIO.output(LED[j], True)
        time.sleep(0.05)
        for j in range(4):
            GPIO.output(LED[j], False)
        time.sleep(0.05)

GPIO.cleanup()
