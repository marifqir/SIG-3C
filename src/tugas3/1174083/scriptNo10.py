# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:33:59 2019

@author: bakti
"""
import shapefile #mengimport shapefile

sf = shapefile.Reader("contohFile") #untuk membaca file tanpa menggunakan ekstensi
isidata = sf.records() #sf.records maksudnya berisikan data dbfberisikan data dbf
print(isidata) #mencetak isi data

# In[]