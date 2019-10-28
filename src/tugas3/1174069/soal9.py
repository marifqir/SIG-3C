# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:54:43 2019

@author: FannyShafira
"""

import shapefile #mengimport shapefile
sf = shapefile.Reader("NamaFile") #digunakan untuk membaca file tanpa menggunakan ekstensi
namakolom = sf.fields #berisikan field-field apa saja yang ada di dalam file dbf
print(namakolom) #mencetak nama kolom

# In[]