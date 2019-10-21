# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:00:24 2019

@author: Aulyardha Anindita
"""

#Nomor 5

import shapefile # mengimport library shapefile
w = shapefile.Writer('Nomor5', shapeType=3) # Membuat writer

w.field("kolom1","C")  # Membuat table dengan kolom pertama
w.field("kolom2","C")  # Membuat table dengan kolom kedua
 
w.record("ngek","satu") # mengisi table untuk kolom pertama dan kedua

w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar

w.close() # Menutup writer