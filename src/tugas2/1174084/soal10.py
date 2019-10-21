# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 12:12:28 2019

@author: rezas
"""

import shapefile #import library shapefile
w=shapefile.Writer('soal10', shapeType=5) #membuat instansiasi shapefile yang memiliki dua parameter("namafile" dan "bentukny")
# In[]
w.shapeType #melihat type/bentuk yang digunakan
# In[]
w.field("kolom1","C") #Membuat table dengan kolom pertama
w.field("kolom2","C") #Membuat table dengan kolom kedua
# In[]
w.record("happy","satu") #Mengisi table pada kolom satu yaitu happy dan kolom dua yaitu satu
w.record("birthday","dua") #Mengisi table pada kolom satu yaitu birthday dan kolom dua yaitu dua
w.record("to","tiga") #Mengisi table pada kolom satu yaitu to dan kolom dua yaitu tiga
w.record("you","empat") #Mengisi table pada kolom satu yaitu you dan kolom dua yaitu empat
w.record("ngek","lima") #Mengisi table pada kolom satu yaitu ngek dan kolom dua yaitu lima
w.record("ngok","enam") #Mengisi table pada kolom satu yaitu ngok dan kolom dua yaitu enam
w.record("ngik","tujuh") #Mengisi table pada kolom satu yaitu ngik dan kolom dua yaitu tujuh
w.record("ngak","delapan") #Mengisi table pada kolom satu yaitu ngak dan kolom dua yaitu delapan
# In[]
w.poly([[[-2,4],[3,4],[5,7],[0,7],[-2,4]]]) #membuat bidang dengan cara menghubungkan garis dari setiap titik koordinat yang digambar
w.poly([[[-2,-1],[3,-1],[5,2],[0,2],[-2,-1]]]) #membuat bidang dengan cara menghubungkan garis dari setiap titik koordinat yang digambar
w.poly([[[-2,-6],[3,-6],[5,-3],[0,-3],[-2,-6]]]) #membuat bidang dengan cara menghubungkan garis dari setiap titik koordinat yang digambar
w.poly([[[-2,-11],[3,-11],[5,-8],[0,-8],[-2,-11]]]) #membuat bidang dengan cara menghubungkan garis dari setiap titik koordinat yang digambar
w.poly([[[8,4],[13,4],[15,7],[10,7],[8,4]]]) #membuat bidang dengan cara menghubungkan garis dari setiap titik koordinat yang digambar
w.poly([[[8,-1],[13,-1],[15,2],[10,2],[8,-1]]]) #membuat bidang dengan cara menghubungkan garis dari setiap titik koordinat yang digambar
w.poly([[[8,-6],[13,-6],[15,-3],[10,-3],[8,-6]]]) #membuat bidang dengan cara menghubungkan garis dari setiap titik koordinat yang digambar
w.poly([[[8,-11],[13,-11],[15,-8],[10,-8],[8,-11]]]) #membuat bidang dengan cara menghubungkan garis dari setiap titik koordinat yang digambar
# In[]
w.close() #Menutup penggambar (writer) 