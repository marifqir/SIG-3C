# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:04:21 2019

@author: bakti
"""
import shapefile #mengimprot shapefile

sf = shapefile.Reader("contohFile") #untuk membaca file tanpa menggunakan ekstensi
sf.shapeType=1 #untuk membaca type shape berapakah yang digunakan

# In[]