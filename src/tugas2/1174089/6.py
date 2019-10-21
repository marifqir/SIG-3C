# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:11:06 2019

@author: ADVENT
"""
import shapefile # Meng-import library shapefile
w = shapefile.Writer('6', shapeType=5) # untuk Membuat penggambar pada shapefile yang nantinya akan di namakan nomor6 dan bentuknya itu adalah shapetype 5 yaitu Polygon

w.field("kolom1","C")  # untuk Membuat table dengan kolom pertama
w.field("kolom2","C")  # untuk Membuat table dengan kolom kedua
 
w.record("ngek","satu") #  untuk Mengisi table yaitu ngek adalah isi pada kolom1 dan satu adalah isi pada kolom2

w.poly([[[1,3],[5,3]]]) #untuk membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang

w.close() # Menutup (writer) karena kita sudah beres menggambar yang kita perlukan 