# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:57:59 2019

@author: acer
"""

import shapefile 
sf = shapefile.Reader("soal3") 
# In[]: mengetahui canvasnya
sf.bbox 