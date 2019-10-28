# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:03:10 2019

@author: acer
"""

import shapefile 
sf = shapefile.Reader("soal5") 
anu=sf.shapes() 
# In[]: untuk mengetahui isiya objek tersebut apa aja
dir(anu) 
dir(anu[0]) 