# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:11:03 2019

@author: acer
"""

import shapefile 
sf = shapefile.Reader("soal2") 
# In[]: 
anu=sf.shapes() 
anu[0].points 