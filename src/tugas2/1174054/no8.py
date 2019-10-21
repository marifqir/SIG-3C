# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:10:28 2019

@author: Aulyardha Anindita
"""

import shapefile # mengimport library shapefile
w = shapefile.Writer('Nomor8', shapeType=5) # Membuat writer

w.field("kolom1","C")  # Membuat table dengan kolom pertama
w.field("kolom2","C")  # Membuat table dengan kolom kedua
 
w.record("ngek","satu") # mengisi table untuk kolom pertama dan kedua

w.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar
w.close() #menutup writer