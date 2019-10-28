# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:12:13 2019

@author: bakti
"""
import shapefile #Meng-import library shapefile

w=shapefile.Writer('contohFile', shapeType=1) #membuat file shp

w.field("kolom1","C") #membuat tabel dengan kolom pertama
w.field("kolom2","C") #membuat tabel dengan kolom kedua
 
w.record("ngek","satu") #tabel ngek memiliki isi dari kolom1 dan satu dari kolom2
w.record("ngok","dua") #tabel ngok memiliki isi dari kolom1 dan dua dari kolom2

w.point(1,1) #membuat point(titik) dengan x=1 dan y=1
w.point(2,2) #membuat point(titik) dengan x=2 dan y=2

w.close()#penutup