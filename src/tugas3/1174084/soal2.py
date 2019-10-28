# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 07:59:27 2019

@author: rezas
"""

import shapefile #import library shapefile
sf = shapefile.Reader("soal1") #membuat instansiasi shapefile yang berfungsi untuk membaca file yang memiliki parameter("namafile")
# In[]
sf.shapeType #melihat type/bentuk yang digunakan
 