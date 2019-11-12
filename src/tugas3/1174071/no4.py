# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:10:47 2019

@author: lenovo
"""

import shapefile 
sf = shapefile.Reader("soal10") 
# In[] : menghitung jumlah yang dibaca oleh variable anu
anu=sf.shapes() 
len(anu)
