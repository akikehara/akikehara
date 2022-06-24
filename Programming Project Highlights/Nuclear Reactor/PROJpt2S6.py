#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:22:11 2020

@author: adam
Adam Ikehara
ECEP 402
PROJ Pt 2, Section 6

The reactor has the control rod full removed. Plot the reactor power for the 
first two seconds after removal. 


CIF = 0
reactivity = .3643
inhour in matlab to get period =  .0028
"""
import matplotlib.pyplot as plt
import math 

#Initial 
T = .0028
P0 = 10
P = P0
t = 0. 
dt = .1

tlist = []
plist = []

while t <= 2.:
    P = P0*math.exp(t/T)
    tlist.append(t)
    plist.append(P)
    t+= dt



plt.figure()
plt.title("Power vs Time (Fully Removed)")
plt.plot(tlist,plist)
plt.xlabel("time (sec)")
plt.ylabel("Power (MW)")
plt.show()
