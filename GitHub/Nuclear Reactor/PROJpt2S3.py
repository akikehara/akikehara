# -*- coding: utf-8 -*-
"""
Adam Ikehara
ECEP 402
PROJ Pt 2, Section 3

Determine and plot the reactor power and period whe the control rod drops from
the height where the reactor is critical to the bottom of the reactor (fully
inserted)

Set CIF = 0, reactivity = -.09929, lambda = .001

"""
import matplotlib.pyplot as plt
import math 

#Initial 
T = -80.9645
P0 = 10
P = P0
t = 0. 
dt = 1.

tlist = []
plist = []

while P >= .01:
    P = P0*math.exp(t/T)
    tlist.append(t)
    plist.append(P)
    t+= dt



plt.figure()
plt.title("Power vs Time (rod fully inserted))")
plt.plot(tlist,plist)
plt.xlabel("time (sec)")
plt.ylabel("Power (MW)")
plt.show()