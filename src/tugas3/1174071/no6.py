# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:15:30 2019

@author: lenovo
"""

import shapefile 
sf = shapefile.Reader("soal10") 
# In[]: untuk melihat jenis shape file pada objek array
anu=sf.shapes() 
anu[0].shapeType