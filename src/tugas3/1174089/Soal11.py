# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:42:58 2019

@author: ADVENT
"""

import shapefile # Meng-import library shapefile
sf = shapefile.Reader("No10") # untuk membaca file dari nama filenya tanpa ekstensi
isiData = sf.records() # Untuk membaca isi record dari file shp yang kita baca dan memasukkannya kedalam variable
print(isiData[0]) # Menampilkan isi dari variable array pertama
print(isiData[0][0]) # Menampilkan isi dari variable multi array