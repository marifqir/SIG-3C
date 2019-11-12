# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:20:58 2019

@author: lenovo
"""
import shapefile 
sf = shapefile.Reader("soal10")
# In[]: membaca data dalam bentuk parts/menyatukan beberapa parts menjadi satu variable record (untuk polyline atau polygon)
anu=sf.shapes()
anu[0].parts 