# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:48:07 2019

@author: FannyShafira
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #menyimpan didalam varaible anu
len(anu) #menghitung jumlah variable anu

# In[]