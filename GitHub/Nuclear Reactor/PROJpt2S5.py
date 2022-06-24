#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:13:05 2020

@author: adam
Adam Ikehara
ECEP 402
PROJ Pt 2, Section 5

The reactor has the control rod removed by 2% of  ritical heiight. Plot the 
reactor ower until the reactor is at 15MW

(insertion depth - (.02*height))/(height)

(830.95 - (.02*1267.68))/(1267.68) = .63549

CIF = .63549, reactivity = .01569, use inhour on matlab to find period

"""
import matplotlib.pyplot as plt
import math 

#Initial 
T = .1060
P0 = 10
P = P0
t = 0. 
dt = .0001

tlist = []
plist = []

while P <= 15:
    P = P0*math.exp(t/T)
    tlist.append(t)
    plist.append(P)
    t+= dt



plt.figure()
plt.title("Power vs Time (2% Rod Removed)")
plt.plot(tlist,plist)
plt.xlabel("time (sec)")
plt.ylabel("Power (MW)")
plt.show()