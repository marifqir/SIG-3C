# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:15:12 2019

@author: Aulyardha Anindita
"""

import shapefile #mengimport library shapefile
w = shapefile.Writer('Nomor9', shapeType=5) # Membuat writer

w.field("kolom1","C")  # Membuat table dengan kolom pertama
w.field("kolom2","C")  # Membuat table dengan kolom kedua
 
w.record("ngek","satu") # Mengisi untuk table yaitu ngek adalah isi pada kolom1 dan satu adalah isi pada kolom2
w.record("crot","dua")  # Mengisi untuk table yaitu ngok adalah isi pada kolom1 dan satu adalah isi pada kolom2

w.poly([[[1,3],[5,3],[5,2],[1,2],[1,3]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[1,6],[5,6],[5,9],[1,9],[1,6]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang 

w.close() #menutup writer