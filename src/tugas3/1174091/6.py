# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:46:37 2019

@author: User
"""

import shapefile #mengimport library
sf = shapefile.Reader("Nomor1") #membaca file shapefile
anu=sf.shapes() #menyimpan hasil kedalam variable anu
print(anu[0].shapeType) #melihat shapetype didalam array 