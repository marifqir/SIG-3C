# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:24:18 2019

@author: HP
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #menyimpan didalam varaible anu
len(anu) #menghitung jumlah variable anu

# In[]