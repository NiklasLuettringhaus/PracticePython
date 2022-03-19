#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED = [18,25]
GPIO.setup(LED[0], GPIO.OUT)
GPIO.setup(LED[1], GPIO.OUT)

print("Strg+C beendet das Programm")

p = GPIO.PWM(LED[0], 50)
q = GPIO.PWM(LED[1], 50)
p.start(0)
q.start(0)

try:
    while True:
        for c in range(0, 101, 2):
            p.ChangeDutyCycle(c)
            q.ChangeDutyCycle(c)
            time.sleep(0.1)
        q.ChangeFrequency(10)
        for c in range(0, 101, 2):
            p.ChangeDutyCycle(100-c)
            q.ChangeDutyCycle(c)
            time.sleep(0.1)
        q.ChangeFrequency(50)

except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
