#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 12:22:40 2021

@author: adam

Compton Continuum 
"""

import matplotlib.pyplot as plt
import pandas as pd

#Read Co-60 spectrum from excel
co60 = pd.read_excel("Co60data.xlsm")
#Convert columns to list
data1 = co60.values.T[0].tolist()
data2 = co60.values.T[1].tolist()

#lists for selected data
channel = []
counts = []

#fills list with selected data
for i in range(980,1200):
    channel.append(data1[i])
    counts.append(data2[i])

def mycolors():
    color = []
    for i in range(0,220):
        if 980 <= channel[i]:
            if channel[i] <=1125:
                color.append('r')
            else:
                color.append('b')
        else:
            color.append('b')
            
    return color

#Plotting
plt.figure()
plt.bar(channel, counts, color = mycolors())
plt.yscale('log')
plt.title("Compton Continuum and First Peak")
plt.ylabel("Counts (log scale)")
plt.xlabel("Channel")
plt.show()
