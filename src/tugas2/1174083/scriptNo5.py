# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:19:41 2019

@author: bakti
"""
import shapefile #Meng-import library shapefile

w=shapefile.Writer('soal5', shapefile=3) #Membuat file dengan nama soal5.shp 
                                        #dan mendefinisikan shapefile 3= POLYLINE

w.field("kolom1","C") #Membuat tabel dengan kolom pertama
w.field("kolom2","C") #Membuat tabel dengan kolom kedua

w.record("ngek","satu") #tabel ngek memiliki isi dari kolom1 dan satu dari kolom2

w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) 
#membuat garis dengan menghubungkan titik titik yang dibuat

w.close() #penutup