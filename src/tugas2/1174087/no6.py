# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 17:02:56 2019

@author: PandA23
"""

import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor6', shapeType=5) # Membuat penggambar pada shapefile yang akan 
                                            #di namakan nomor6 dan bentuknya  adalah shapetype 5 yaitu Polygon

w.field("kolom1","C")  # Membuat table dengan kolom pertama
w.field("kolom2","C")  # Membuat table dengan kolom kedua

w.record("ngek","satu") # Mengisi untuk table yaitu ngek adalah isi pada kolom1 dan satu adalah isi pada kolom2

w.poly([[[1,3],[5,3]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar 

w.close() # Menutup penggambar (writer) karena kita sudah selsai menggambar yang kita gambar