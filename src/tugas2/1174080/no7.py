# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:37:56 2019

@author: HP
"""

import shapefile # Mengimportkan library shapefile
w = shapefile.Writer('Nomor7', shapeType=5) # Menggambar pada shapefile yang nantinya akan di namakan nomor7 dan bentuknya itu adalah shapetype 5 yaitu Polygon

w.field("kolom1","C")  # Membuatkan table dengan kolom pertama
w.field("kolom2","C")  # Membuatkan table dengan kolom kedua
 
w.record("ngek","satu") # Untuk table yaitu ngek adalah isi pada kolom1 dan satu adalah isi pada kolom2
 
w.poly([[[1,3],[5,3],[1,2],[5,2]]]) # MembuatKAN garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang

w.close() # Menutup writer