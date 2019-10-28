# -*- coding: utf-8 -*-
"""
@author: D. Irga B. Naufal Fakhri
"""
import shapefile # Meng-import library shapefile
sf = shapefile.Reader("Nomor10") # Berguna untuk membaca file dari nama filenya tanpa ekstensi
isiData = sf.records() # Untuk membaca isi record dari file shp yang kita baca dan memasukkannya kedalam variable
print(isiData) # Menampilkan isi dari variable