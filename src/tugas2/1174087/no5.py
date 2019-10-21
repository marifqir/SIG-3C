# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:50:45 2019

@author: PandA23
"""

import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor5', shapeType=3) # Membuat penggambar pada shapefile yang akan 
                                            #di namakan nomor5 dan bentuknya adalah shapetype 3 yaitu PolyLine (Garis)

w.field("kolom1","C")  # Membuat table dengan kolom pertama
w.field("kolom2","C")  # Membuat table dengan kolom kedua

w.record("ngek","satu") # Mengisi untuk table yaitu ngek adalah isi pada kolom1 dan satu adalah isi pada kolom2

w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar

w.close() # Menutup penggambar (writer) karena kita sudah selsai menggambar yang kita gambar