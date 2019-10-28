# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:14:25 2019

@author: PandA23
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("contohaja") #digunakan untuk membaca file 
anu=sf.shapes() #untuk menyimpan variable sf di dalam anu
#%%
anu[0].shapeType #membaca data di dalam variable anu yang pertama