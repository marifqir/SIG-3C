# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:09:56 2019

@author: bakti
"""
import shapefile #Meng-import library shapefile

w=shapefile.Writer('soal4', shapefile.POINT) #Membuat file dengan nama soal4.shp
                                #dan mendefinisikan shapefile.POINT = point/titik

w.field("kolom1","C") #Membuat tabel dengan kolom pertama
w.field("kolom2","C") #Membuat tabel dengan kolom kedua

w.record("ngek","satu") #tabel ngek memiliki isi dari kolom1 dan satu dari kolom2
w.record("ngok","dua") #tabel ngok memiliki isi dari kolom1 dan dua dari kolom2

w.point(1,1) #membuat point(titik) dengan x=1 dan y=1
w.point(2,2) #membuat point(titik) dengan x=2 dan y=2

w.close() #penutup