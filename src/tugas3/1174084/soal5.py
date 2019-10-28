# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:02:06 2019

@author: rezas
"""

import shapefile #import library shapefile
sf = shapefile.Reader("soal1") #membuat instansiasi shapefile yang berfungsi untuk membaca file yang memiliki parameter("namafile")
# In[]
anu=sf.shapes() #membuat variabel anu yang menampung daftar geometri shapefile
# In[]
dir(anu) #menunjukkan kita semua metode yang tersedia untuk objek anu
# In[]
dir(anu[0]) #menunjukkan kita semua metode yang tersedia untuk objek anu pada index 0