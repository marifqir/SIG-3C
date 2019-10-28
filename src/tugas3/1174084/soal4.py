# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:01:01 2019

@author: rezas
"""

import shapefile #import library shapefile
sf = shapefile.Reader("soal1") #membuat instansiasi shapefile yang berfungsi untuk membaca file yang memiliki parameter("namafile")
# In[]
anu=sf.shapes() #membuat variabel anu yang menampung daftar geometri shapefile
# In[]
len(anu) #Metode bentuk mengembalikan daftar objek Bentuk yang menggambarkan geometri dari setiap shape record