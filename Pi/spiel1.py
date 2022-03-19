#!/usr/bin/python
import random
zahl = random.randrange(0,1000)
tipp = 0
i = 0

while tipp != zahl:
    tipp = int(input("Dein Tipp:"))
    if zahl < tipp:
        print("Die gesuchte Zahl ist kleiner als ",tipp)

    if zahl > tipp:
        print("Die gesuchte Zahl ist größer als ",tipp)

    i += 1
print("Du hast die Zahl beim ",i,". Tipp erraten")
