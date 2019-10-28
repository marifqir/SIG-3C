# -*- coding: utf-8 -*-
"""
@author: D. Irga B. Naufal Fakhri
"""
import shapefile # Meng-import library shapefile
sf = shapefile.Reader("Nomor10") # Berguna untuk membaca file dari nama filenya tanpa ekstensi
isiData = sf.records() # Untuk membaca isi record dari file shp yang kita baca dan memasukkannya kedalam variable
print(isiData[0]) # Menampilkan isi dari variable array pertama
print(isiData[0][0]) # Menampilkan isi dari variable multi array