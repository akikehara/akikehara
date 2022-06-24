#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 13:27:41 2021

@author: Adam Ikehara

Gamma Spectroscopy for Co-60, selected region to highlight the compton edges 
and peaks to perform compton-peak ratio analysis

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
for i in range(800,1500):
    channel.append(data1[i])
    counts.append(data2[i])


#function for color range
def mycolors():
    #empty color list for each hist bar
    color = []
    #loop to assign each bar and append list, 0-700 because len(channel)
    for i in range(0,700):
        #980 beginning of edge
        if 980 <= channel[i]:
            #1125 end of egde
            if channel[i] <=1125:
                color.append('r')
                
            else:
                color.append('b')
        else:
            color.append('b')
            
    return color

#Plotting
plt.figure()
plt.bar(channel, counts, color = mycolors() )
plt.yscale('log')
plt.title("Gamma Spectrum of Cobalt-60")
plt.ylabel("Counts (log scale)")
plt.xlabel("Channel")
plt.show()
