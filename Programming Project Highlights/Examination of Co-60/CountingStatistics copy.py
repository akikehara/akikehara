#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 12:11:26 2022

@author: Adam Ikehara

ECEP 372
Lab 3 - Counting Statistics

1) Remove First and Last Points as these are partial counts
2) Combine each Station together
3) Charts
    * Histogram of each station w/ best fitted curve gaussian
    * CDF Plot of each station
    * Norm Plot of each
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm
from scipy import stats

##Loads csv data & makes them lists
def loadjoin(filename):
    dataframe = pd.read_csv(filename, delimiter=',', header =None)
    datalist = []
    for i in range(0,6):
        x = dataframe[i].values.tolist()
        datalist.extend(x)
    return datalist

##Gaussian Curve fitting Function
def curvefit(file):
    mean,std = norm.fit(loadjoin(file))
    xmin = min(loadjoin(file))
    xmax = max(loadjoin(file))
    x = np.linspace(xmin, xmax, 100)
    y = norm.pdf(x, mean, std)
    return (x , y)

##CDF Plot function
def cdfplot(file):
    f = loadjoin(file)
    x = np.sort(f)
    #calculate CDF values
    y = 1. * np.arange(len(f)) / (len(f) - 1)
    return (x, y)

##Norm Plot function
def normplot(file):
    (quantiles, values), (slope, intercept, r) = stats.probplot(loadjoin(file), dist='norm')
    return values, quantiles, slope, intercept

#Number of bins (Scott's Rule)
def nbins(file):
    data = np.array(loadjoin(file))
    n = len(data)
    bins = math.floor(3.49 * data.std() * n ** (-1/3))
    return bins

##nameing the csv's 
file0 = 'Station1Data.csv' 
file1 = 'Station2Data.csv'
file2 = 'Station3Data.csv'
file3 = 'Station4Data.csv'

##Plotting Histograms
fig, ax = plt.subplots(2, 2,figsize =[13,8])
plt.suptitle('Histograms and Best Gaussian Fit')
hist0 = ax[0,0].hist(loadjoin(file0), bins = nbins(file0), density = True, color = 'b')
hist1 = ax[0,1].hist(loadjoin(file1), bins = nbins(file1), density = True, color = 'orange')
hist2 = ax[1,0].hist(loadjoin(file2), bins = nbins(file2), density = True, color = 'forestgreen')
hist3 = ax[1,1].hist(loadjoin(file3), bins = nbins(file3), density = True, color = 'm')

ax[0,0].set_title('Station 1')
ax[0,1].set_title('Station 2')
ax[1,0].set_title('Station 3')
ax[1,1].set_title('Station 4')

##Plotting Gaussian Curve Fit
x0, y0 = curvefit(file0)
x1, y1 = curvefit(file1)
x2, y2 = curvefit(file2)
x3, y3 = curvefit(file3)

ax[0,0].plot(x0, y0,'--', color = 'k')
ax[0,1].plot(x1, y1,'--', color = 'k')
ax[1,0].plot(x2, y2,'--', color = 'k')
ax[1,1].plot(x3, y3,'--', color = 'k')
plt.show()

##CDF Plots
fig, ax = plt.subplots(2,2, figsize  = [13,8])
ax[0,0].set_title('Station 1')
ax[0,1].set_title('Station 2')
ax[1,0].set_title('Station 3')
ax[1,1].set_title('Station 4')

a, b = cdfplot(file0)
c, d = cdfplot(file1)
e, f = cdfplot(file2)
g, h = cdfplot(file3)

plt.suptitle('CDF Plots')
cdf0 = ax[0,0].plot(a,b, color = 'b')
cdf0 = ax[0,1].plot(c,d, color = 'orange')
cdf1 = ax[1,0].plot(e,f, color = 'forestgreen')
cdf2 = ax[1,1].plot(g,h, color = 'm')
plt.show()

##NormPlots
fig, ax = plt.subplots(2,2, figsize = [13,8])
ax[0,0].set_title('Station 1')
ax[0,1].set_title('Station 2')
ax[1,0].set_title('Station 3')
ax[1,1].set_title('Station 4')

v0, q0, s0, i0 =  normplot(file0)
v1, q1, s1, i1 =  normplot(file1)
v2, q2, s2, i2 =  normplot(file2)
v3, q3, s3, i3 =  normplot(file3)

plt.suptitle('NormPlots')
ax[0,0].plot(v0, q0, '+b')
ax[0,0].plot(q0*s0 + i0, q0, 'k')
ax[0,1].plot(v1, q1, '+', color = 'orange')
ax[0,1].plot(q1*s1 + i1, q1, 'k')
ax[1,0].plot(v2, q2, '+', color = 'forestgreen')
ax[1,0].plot(q2*s2 + i2, q2, 'k')
ax[1,1].plot(v3, q3, '+', color = 'm')
ax[1,1].plot(q3*s3 + i3, q3, 'k')

ax[0,0].grid()
ax[0,1].grid()
ax[1,0].grid()
ax[1,1].grid()
plt.show()