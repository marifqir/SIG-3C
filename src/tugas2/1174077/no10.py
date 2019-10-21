# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:52:58 2019

@author: ASUS
"""

import shapefile # import library shapefile
w = shapefile.Writer('no10', shapeType=5)  # menggunakan fungsi writer yang digunakan untuk menggambar dan akan dinamakan no10 dalam bentuk shapetype=5 yang merupakan sebuah polygon
  
w.field("kolom1","C")  # Digunakan untuk membuat kolom pertama pada table
w.field("kolom2","C")  # Digunakan untuk membuat kolom dua pada table
 
w.record("AKU ","SAYANG") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("KAMU ","BOHONG") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("PUSING ","PALA") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("TUGAS ","GERCEP") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("TIPU ","DIA") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("CRAT ","CROT") # mengisi kolum yang sudah dibuat dengan ngek dan satu
w.record("AH ","UDAHLAH") # mengisi kolum yang sudah dibuat dengan ngek dan satu




w.poly([[[-10,0],[-8,-3],[-6,0],[-8,3],[-10,0]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut
w.poly([[[-6,0],[-4,-3],[-2,0],[-4,3],[-6,0]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut
w.poly([[[-2,0],[0,-3],[2,0],[0,3],[-2,0]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut
w.poly([[[-2,6],[0,3],[2,6],[0,9],[-2,6]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut
w.poly([[[-2,-6],[0,-9],[2,-6],[0,-3],[-2,-6]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut
w.poly([[[2,0],[4,-3],[6,0],[4,3],[2,0]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut 
w.poly([[[10,0],[8,-3],[6,0],[8,3],[10,0]]]) # menghubungkan garis dengan mendefinisikan setiap titik awal dan akhir dari garis tersebut 

w.close() # Menutup writer