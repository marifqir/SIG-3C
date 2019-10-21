# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:04:13 2019

@author: ASUS
"""

import shapefile # import library shapefile
w = shapefile.Writer('no3', shapeType=1)  # menggunakan fungsi writer yang digunakan untuk menggambar dan akan dinamakan no3 dalam bentuk shapetype=1 yang merupakan sebuah titik
 
w.field("kolom1","C")  # Digunakan untuk membuat kolom pertama pada table
w.field("kolom2","C")  # Digunakan untuk membuat kolom dua pada table
 
w.record("ngek","satu") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("ngok","dua")  # mengisi kolum yang sudah dibuat dengan ngek dan satu
 
w.point(1,1) #  mendefinisikan point di koordinat  1,1
w.point(2,2) #  mendefinisikan point di koordinat  2,2

w.close() # Menutup writer