# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:33:44 2019

@author: bakti
"""
import shapefile #mengimport shapefile

sf = shapefile.Reader("contohFile") #untuk membaca file tanpa menggunakan ekstensi
namakolom = sf.fields #berisikan field-field apa saja yang ada di dalam file dbf
print(namakolom) #mencetak nama kolom

# In[]