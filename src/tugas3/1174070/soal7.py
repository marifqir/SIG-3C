# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:50:52 2019

@author: User
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("bacafile") #digunakan untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #untuk menyimpan variable sf di dalam anu
anu[0].parts #membaca data di dalam variable anu yang pertama parts adalah dua record yang dijadikan satu

# In[]NamaFile