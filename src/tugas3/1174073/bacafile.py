# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:31:04 2019

@author: Ainul Filiani
"""

import shapefile # mengimport library shapefile
w=shapefile.Writer("baca file", shapeType=1) # Membuat writer

w.field("kolom1","C") # Membuat table dengan kolom pertama
w.field("kolom2","C") # Membuat table dengan kolom kedua

w.record("ngek","satu") # mengisi table untuk kolom pertama dan kedua
w.record("ngok","dua")

w.point(1,1) #membuat garis dengan cara menghubungkan setiap titik yang digambar
w.point(2,2)

w.close() #menutup writer