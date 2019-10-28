# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:29:01 2019

@author: USER
"""

import shapefile 
sf = shapefile.Reader("soal4") 
anu=sf.shapes() #untuk mengambil semua record data geometric
anu[0].shapeType #membaca shapeType anu

# In[]