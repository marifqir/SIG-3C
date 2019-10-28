# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:25:35 2019

@author: USER
"""

import shapefile 
sf = shapefile.Reader("soal4") 
anu=sf.shapes() #untuk menngambil semua record data geomtric
len(anu) #untuk menghitung jumlah variable anu

# In[]