# -*- coding: utf-8 -*-
"""
@author: D. Irga B. Naufal Fakhri
"""
import shapefile # Meng-import library shapefile
sf = shapefile.Reader("Nomor10") # Berguna untuk membaca file dari nama filenya tanpa ekstensi
namaKolom = sf.fields # Memasukkan nama fields dari file shp yang kita baca kedalam variable
print(namaKolom) # Menampilkan isi dari variable namaKolom