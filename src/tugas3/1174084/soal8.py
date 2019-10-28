# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:03:46 2019

@author: rezas
"""

import shapefile #import library shapefile
sf = shapefile.Reader("soal1") #membuat instansiasi shapefile yang berfungsi untuk membaca file yang memiliki parameter("namafile")
# In[]
anu=sf.shapes() #membuat variabel anu yang menampung daftar geometri shapefile
# In[]
anu[0].points #melihat daftar tupel yang berisi koordinat (x, y) untuk setiap titik dalam bentuk pada variabel anu index 0