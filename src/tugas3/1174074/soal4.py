# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:11:17 2019

@author: Aspire E15
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #menyimpan didalam varaible anu
len(anu) #menghitung jumlah variable anu
# In[]
