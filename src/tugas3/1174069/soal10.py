# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:55:46 2019

@author: FannyShafira
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
isidata = sf.records() #sf.records maksudnya berisikan data dbfberisikan data dbf
print(isidata) #mencetak isi data

# In[]