#!/usr/bin/python
import time, random
from tkinter import *

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
vw = DoubleVar()
vw.set(" -  -  - ")

def wurf():
    ez = vz.get()
    ea = va.get()
    w = ""
    for i in range(ez):
        w += str(random.randrange(1, ea + 1))
        if i < ez -1:
            w += " - "
    vw.set(w)

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
      textvariable=vw,
      fg="red",
      bg="yellow",
      font="Verdana 12 bold").grid(row=5,column=1)
            
Button(root,
       text="Würfeln",
       command=wurf).grid(row=5,column=0)

root.mainloop()
