# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:04:24 2019

@author: rezas
"""

import shapefile #import library shapefile
sf = shapefile.Reader("soal1") #membuat instansiasi shapefile yang berfungsi untuk membaca file yang memiliki parameter("namafile")
# In[]
namakolom = sf.fields #membuat variabel namakolom yang menampung daftar tabel 
# In[] 
print(namakolom) #menampilkan variabel namakolom