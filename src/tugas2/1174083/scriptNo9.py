# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 00:01:46 2019

@author: bakti
"""
import shapefile #Meng-import library shapefile

w=shapefile.Writer('soal9', shapeType = 5) #Membuat file dengan soal9.shp 
                                        #dan mendefinisikan shapefile 5 = POLYGON

w.field("kolom1","C") #Membuat tabel dengan kolom pertama
w.field("kolom2","C") #Membuat tabel dengan kolom kedua

w.record("ngek","satu") #tabel ngek memiliki isi dari kolom1 dan satu dari kolom2
w.record("crot","dua") #tabel ngek memiliki isi dari kolom1

w.poly([[[1,3],[5,3],[5,2],[1,2],[1,3]]]) 
#membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan

w.poly([[[1,6],[5,6],[5,9],[1,9],[1,6]]]) 
#membuat garis dengan menghubungkan titik titik yang dibuat dan memberi warna di dalam garis yg di hubungkan

w.close() #penutup