#!/usr/bin/python
import RPi.GPIO as GPIO
import time

LED = 25
PIZ = 18
f = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(PIZ,GPIO.OUT)
metronomL = GPIO.PWM(LED,f)
metronomP = GPIO.PWM(PIZ,f)

metronomL.start(1)
metronomP.start(1)
metronomL.ChangeDutyCycle(25)

print("Strg+C beendet das Programm")
try:
    while True:
        pass

except KeyboardInterrupt:
    for i in range(8):
        f *= 2
        metronomL.ChangeFrequency(f)
        metronomP.ChangeFrequency(f)
        time.sleep(0.25)

    metronomL.stop()
    metronomP.stop()
    GPIO.cleanup()
