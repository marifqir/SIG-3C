# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:59:13 2019

@author: acer
"""

import shapefile 
sf = shapefile.Reader("soal4") 

# In[] : mengetahui panjangnya.
anu=sf.shapes() 
len(anu)