# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 18:54:21 2018

@author: Abhishek
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

os.getcwd()
os.chdir('C:/Users/Abhishek/Desktop/')

toplist = pd.read_csv("top500list1.csv",encoding='latin1')
toplist

list(toplist)

toplist[' Cores'].describe()
toplist[' Rmax (TFlop/s)'].describe()
toplist[' Rpeak (TFlop/s)'].describe()
toplist[' Power (kW)'].describe()

toplist.head()
toplist.tail()

toplist.info()

plt.scatter(toplist[' Cores'],toplist[' Rpeak (TFlop/s)'])
plt.scatter(toplist[' Cores'],toplist[' Power (kW)'])



