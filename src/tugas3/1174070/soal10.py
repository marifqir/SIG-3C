# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 20:51:55 2019

@author: User
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
isidata = sf.records() #sf.records maksudnya berisikan data dbfberisikan data dbf
print(isidata) #mencetak isi data

# In[]