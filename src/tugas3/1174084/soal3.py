# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 07:59:56 2019

@author: rezas
"""

import shapefile #import library shapefile
sf = shapefile.Reader("soal1") #membuat instansiasi shapefile yang berfungsi untuk membaca file yang memiliki parameter("namafile")
# In[]
sf.bbox #Bounding Box yang merepresentasikan titik antara lain xmin,ymin,xmax,ymax