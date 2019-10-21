# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:08:47 2019

@author: ADVENT
"""
import shapefile # Meng-import library shapefile
w = shapefile.Writer('5', shapeType=3) # untuk penggambar pada shapefile yang nantinya akan di namakan nomor5 dan bentuknya itu adalah shapetype 3 yaitu PolyLine (Garis)

w.field("kolom1","C")  # untuk Membuat table dengan kolom pertama
w.field("kolom2","C")  # untuk Membuat table dengan kolom kedua
 
w.record("ngek","satu") #  untuk Mengisi table yaitu ngek adalah isi pada kolom1 dan satu adalah isi pada kolom2

w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) # untuk membuat garis dengan cara menghubungkan setiap titik yang digambar

w.close() # Menutup (writer) karena kita sudah beres menggambar yang kita perlukan