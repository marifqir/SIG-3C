# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:27:21 2019

@author: USER
"""

import shapefile 
sf = shapefile.Reader("soal4") 
anu=sf.shapes()  #untuk mengambil semua data record geometric
dir(anu) #un utk mengambil data objek yaitu anu
dir(anu[0]) 

# In[]