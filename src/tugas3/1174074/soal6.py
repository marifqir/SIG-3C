# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:11:18 2019

@author: Aspire E15
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #untuk menyimpan variable sf di dalam anu
anu[0].shapeType #membaca data di dalam variable anu yang pertama
# In[]
