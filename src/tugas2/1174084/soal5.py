# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:41:43 2019

@author: rezas
"""


import shapefile #import library shapefile
w=shapefile.Writer('soal5', shapeType=3) #membuat instansiasi shapefile yang memiliki dua parameter("namafile" dan "bentukny")
# In[]
w.shapeType #melihat type/bentuk yang digunakan
# In[]
w.field("kolom1","C") #Membuat table dengan kolom pertama
w.field("kolom2","C") #Membuat table dengan kolom kedua
# In[]
w.record("ngek","satu") #Mengisi table pada kolom satu yaitu ngek dan kolom dua yaitu satu
# In[]
w.line([[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #membuat garis dengan cara menghubungkan setiap titik koordinat yang digambar
# In[]
w.close() #Menutup penggambar (writer) 