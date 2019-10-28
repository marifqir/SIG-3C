# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:22:49 2019

@author: bakti
"""
import shapefile #mengimport shapefile

sf = shapefile.Reader("contohFile") #untuk membaca file tanpa menggunakan ekstensi
anu=sf.shapes() #menyimpan didalam varaible anu
len(anu) #menghitung jumlah variable anu

# In[]