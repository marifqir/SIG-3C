# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:55:33 2019

@author: Aulyardha Anindita
"""

#Nomor 3

import shapefile # mengimport library shapefile
w=shapefile.Writer("Nomor 3",shapeType=1) # Membuat writer

w.field("kolom1","C") # Membuat table dengan kolom pertama
w.field("kolom2","C") # Membuat table dengan kolom kedua

w.record("ngek","satu") # mengisi table untuk kolom pertama
w.record("ngok","dua") # mengisi table untuk kolom kedua

w.point(1,1) #membuat garis dengan cara menghubungkan setiap titik yang digambar
w.point(2,2)

w.close() #menutup writer