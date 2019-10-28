# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:05:08 2019

@author: rezas
"""

import shapefile #import library shapefile
sf = shapefile.Reader("soal1") #membuat instansiasi shapefile yang berfungsi untuk membaca file yang memiliki parameter("namafile")
# In[]
isidata = sf.records() #membuat variabel isidata yang menampung daftar data records
# In[]
print(isidata) #menampilkan variabel isidata