# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:07:02 2019

@author: acer
"""

import shapefile 
sf = shapefile.Reader("soal3") 

# In[]:
anu=sf.shapes() 
anu[0].shapeType 