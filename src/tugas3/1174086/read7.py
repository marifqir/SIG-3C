# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:09:16 2019

@author: acer
"""

import shapefile 
sf = shapefile.Reader("soal8")
# In[]:  
anu=sf.shapes() 
anu[0].parts 