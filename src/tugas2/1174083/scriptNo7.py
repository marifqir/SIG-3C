# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 23:47:49 2019

@author: bakti
"""
import shapefile #Meng-import library shapefile

w=shapefile.Writer('soal7', shapefile=3) #Membuat file dengan nama soal7.shp 
                                        #dan mendefinisikan shapefile 3=POLYLINE

w.field("kolom1","C") #Membuat tabel dengan kolom pertama
w.field("kolom2","C") #Membuat tabel dengan kolom kedua

w.record("ngek","satu") #tabel ngek memiliki isi dari kolom1 dan satu dari kolom2

w.poly([[[1,3],[5,3],[1,2],[5,2]]]) #membuat garis dengan menghubungkan titik titik 
                    #yang dibuat dan memberi warna di dalam garis yg di hubungkan

w.close() #penutup