# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:36:54 2019

@author: lenovo
"""

import shapefile 
sf = shapefile.Reader("soal10") 
# In[] : menampilkan record dari shape file
isidata = sf.records() 
print(isidata) 