# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:53:57 2019

@author: FannyShafira
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #untuk menyimpan variable sf di dalam anu
anu[0].points #membaca data di dalam variable anu yang pertama points yaitu berisikan file .shp

# In[]