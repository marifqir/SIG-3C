# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:36:21 2019

@author: HP
"""

import shapefile # mengimportkan library shapefile
w = shapefile.Writer('no1', shapeType=1)  # fungsi writer ini untuk menggambar dan akan dinamakan nomer 1 dalam bentuk shapetype yaitu 1 adalah sebuah titik

w.field("kolom1","C")  # untuk membuat kolom pertama pada table
w.field("kolom2","C")  # untuk membuat kolom kedua pada table
 
w.record("ngek","satu") # untuk mengisi kolum yang telah dibuat dengan ngek dan satu
w.record("ngok","dua")  # untuk mengisi kolum yang telah dibuat dengan ngok dan dua
 
w.point(1,1) # artinya adalah point di koordinat  1,1
w.point(2,2) # artinya adalah point di koordinat  2,2

w.close() # Menutup writer.