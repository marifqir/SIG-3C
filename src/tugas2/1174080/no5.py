# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:53:58 2019

@author: HP
"""

import shapefile # mengimportkan library shapefile
w = shapefile.Writer('no5', shapeType=3)  # yaitu fungsi writer yang digunakan untuk menggambar dan akan dinamakan nomer 5 dalam bentuk shapetype yaitu 3 yang merupakan bentuk polyline
 
w.field("kolom1","C")  # untuk membuat kolom pertama pada table
w.field("kolom2","C")  # untuk membuat kolom dua pada table
 
w.record("ngek","satu") # mengisikan kolum yang sudah dibuat dengan ngek dan satu
 
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan titik akhir dari garis tersebut


w.close() # Menutup writer.