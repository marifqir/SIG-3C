# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:07:30 2019

@author: lenovo
"""

import shapefile 
sf = shapefile.Reader("soal10") 
# In[]: untuk mengetahui canvas atau batas kotaknya (box)
sf.bbox 