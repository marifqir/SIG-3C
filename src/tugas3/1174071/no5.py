# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 00:13:57 2019

@author: lenovo
"""

import shapefile 
sf = shapefile.Reader("soal10") 
anu=sf.shapes() 
# In[]: untuk membaca isi dari variable anu
dir(anu) 
dir(anu[0]) 