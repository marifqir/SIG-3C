# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:21:53 2019

@author: ACER
"""

import shapefile # import library shapefile
w = shapefile.Writer('no1', shapeType=1)  # menggunakan fungsi writer yang digunakan untuk menggambar dan akan dinamakan no1 dalam bentuk shapetype=1 yang merupakan sebuah titik

w.field("kolom1","C")  # Digunakan untuk membuat kolom pertama pada table
w.field("kolom2","C")  # Digunakan untuk membuat kolom kedua pada table
 
w.record("ngek","satu") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("ngok","dua")  # mengisi kolum yang sudah dibuat dengan ngek dan dua
 
w.point(1,1) # mendefinisikan point di koordinat  1,1
w.point(2,2) # mendefinisikan point di koordinat  2,2

w.close() # Menutup writer

