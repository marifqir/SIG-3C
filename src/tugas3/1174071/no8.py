# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:27:52 2019

@author: lenovo
"""

import shapefile 
sf = shapefile.Reader("soal10") 
# In[]: membaca data dalam bentuk points/titik
anu=sf.shapes() 
anu[0].points 