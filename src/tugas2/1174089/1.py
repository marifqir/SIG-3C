# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:50:03 2019

@author: ADVENT
"""

import shapefile # Meng-import library shapefile
w = shapefile.Writer('1', shapeType=1)  # Untuk penggambar pada shapefile yang nantinya akan di namakan nomor1 dan bentuknya itu adalah shapetype 1 yaitu point (titik)
 
w.field("kolom1","C")  # Untuk table dengan kolom pertama
w.field("kolom2","C")  # Untuk table dengan kolom kedua
 
w.record("ngek","satu") #  untuk Mengisi table yaitu ngek adalah isi pada kolom1 dan satu adalah isi pada kolom2
w.record("ngok","dua")  #  untuk Mengisi table yaitu ngok adalah isi pada kolom1 dan satu adalah isi pada kolom2
 
w.point(1,1) # point (titik) pada koordinat x,y yaitu 1,1
w.point(2,2) # point (titik) pada koordinat x,y yaitu 2,2

w.close() # menutup  (writer) karena kita sudah beres menggambar yang kita perlukan