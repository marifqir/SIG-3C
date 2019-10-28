# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:42:58 2019

@author: ADVENT
"""

import shapefile # Meng-import library shapefile
sf = shapefile.Reader("No10") # Berguna untuk membaca file dari nama filenya tanpa ekstensi
namaKolom = sf.fields # Memasukkan nama fields dari fileshp yang kita baca kedalam variable
print(namaKolom) # Menampilkan isi dari variable namaKolom