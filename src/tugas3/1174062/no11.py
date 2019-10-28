# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:36:06 2019

@author: USER
"""

import shapefile 
sf = shapefile.Reader("soal4") 
isidata = sf.records() #untuk mengambil semua record
print(isidata[0]) #adalah untuk mencetak isi data record
print(isidata[0][0]) 

# In[]
