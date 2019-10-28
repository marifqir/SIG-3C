# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:25:42 2019

@author: bakti
"""
import shapefile #mengimport shapefile

sf = shapefile.Reader("contohFile") #untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #untuk menyimpan variable sf di dalam anu
anu[0].shapeType #membaca data di dalam variable anu yang pertama

# In[]