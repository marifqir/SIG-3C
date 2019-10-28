# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:12:54 2019

@author: acer
"""

import shapefile 
sf = shapefile.Reader("soal4") 
# In[]
namakolom = sf.fields 
print(namakolom)