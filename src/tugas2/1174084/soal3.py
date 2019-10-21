# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:39:46 2019

@author: rezas
"""

import shapefile #import library shapefile
w=shapefile.Writer('soal3', shapeType=1) #membuat instansiasi shapefile yang memiliki dua parameter("namafile" dan "bentukny")
# In[]
w.shapeType #melihat type/bentuk yang digunakan
# In[]
w.field("kolom1","C") #Membuat table dengan kolom pertama
w.field("kolom2","C") #Membuat table dengan kolom kedua
# In[]
w.record("ngek","satu") #Mengisi table pada kolom satu yaitu ngek dan kolom dua yaitu satu
w.record("ngok","dua") #Mengisi table pada kolom satu yaitu ngok dan kolom dua yaitu dua
# In[]
w.point(1,1) #Menggambarkan vector point pada koordinat x,y yaitu 1,1
w.point(2,2) #Menggambarkan vecto point pada koordinat x,y yaitu 2,2
# In[]
w.close() #Menutup penggambar (writer) 