# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:15:57 2019

@author: acer
"""

import shapefile 
sf = shapefile.Reader("soal4") 
# In[]
isidata = sf.records() 
print(isidata[0]) 
print(isidata[0][0]) 
 
 