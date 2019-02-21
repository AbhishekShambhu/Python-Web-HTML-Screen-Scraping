# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 01:17:53 2018

@author: Abhishek
"""

import urllib
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

filename = "top500list1.csv"
f = open(filename, "w")

headers = "Rank, Site, System, Cores, Rmax (TFlop/s), Rpeak (TFlop/s), Power (kW)\n"
f.write(headers)
    
for i in range(1,6):
        r = "https://www.top500.org/list/2018/06/?page={}".format(i)
        url=requests.get(r)
        soup = BeautifulSoup(url.content, 'html.parser')
    
        for record in soup.findAll('tr'):
            
            tbltxt = ""

            for data in record.findAll('td'):
                
                    tbltxt = tbltxt.replace("\n","") + data.text.replace(",","") + ","
                    tbltxt
                    print(tbltxt)
            #print(tbltxt)
            
            f.write(tbltxt[0:-1]+"\n")
      
f.close()    

os.getcwd()
os.chdir('C:/Users/Abhishek/Desktop/')

list1 = pd.read_csv("top500list1.csv", encoding='latin1')

list1['Country'].describe()
plt.style.use('ggplot')
list1.groupby(['Country']).Country.count().plot.bar(legend=True)
plt.show()



# display the record; drop the trailing comma
#filename = pd.DataFrame(filename. Site.str.split(' ',1).tolist(),columns = ['Site','Country'])
#print(tbltxt)

#f.close()

list1['Country'].describe()









