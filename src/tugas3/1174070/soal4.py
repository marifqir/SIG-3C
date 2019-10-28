# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:49:21 2019

@author: User
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #menyimpan didalam varaible anu
len(anu) #menghitung jumlah variable anu

# In[]