# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:35:17 2019

@author: HP
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
namakolom = sf.fields #berisikan field-field apa saja yang ada di dalam file dbf
print(namakolom) #mencetak nama kolom

# In[]