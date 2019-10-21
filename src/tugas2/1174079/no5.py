# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 07:44:38 2019

@author: ACER
"""

import shapefile # import library shapefile
w = shapefile.Writer('no5', shapeType=3)  # menggunakan fungsi writer yang digunakan untuk menggambar dan akan dinamakan no5 dalam bentuk shapetype=3 yang merupakan sebuah polyline
 
w.field("kolom1","C")  # Digunakan untuk membuat kolom pertama pada table
w.field("kolom2","C")  # Digunakan untuk membuat kolom dua pada table
 
w.record("ngek","satu") # mengisi kolum yang sudah dibuat dengan ngek dan satu
 
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut


w.close() # Menutup writer