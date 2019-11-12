# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:38:36 2019

@author: lenovo
"""

import shapefile 
sf = shapefile.Reader("soal10") 
# In[] : menampilan record dalam bentuk array dan multi array
isidata = sf.records() 
print(isidata[0]) 
print(isidata[0][0]) 