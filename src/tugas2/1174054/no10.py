# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:18:39 2019

@author: Aulyardha Anindita
"""

#Nomor 10
import shapefile #Berfungsi untuk mengimport library shapefile
w = shapefile.Writer("Nomor10", shapeType=5) #membuat writer dengan nama nomor10 yang dimana bentuknya adalah shapetype =5

w.field("Aulya","C") # Membuat table kolom pertama
w.field("Ardha","C") # Membuat table kolom kedua

w.record("LeeJongSuk","JiChangWook") #Membuat isi table pada kolom pertama
w.record("LeeSeungGi","LeeMinHoo") #Membuat isi table pada kolom kedua
w.record("YooSeungHoo","ParkSooHyun") #Membuat isi table pada kolom ketiga
w.record("SongJongki","LeeKwangSoo") # Membuat isi table pada kolom keempat
w.record("ParkHyungSik","SoJiSub") #Membuat isi table pada kolom kelima

w.poly([[[-6,2],[3,-2],[5,3],[-4,3],[-6,2]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang 
w.poly([[[2,3],[5,3],[6,1],[1,1],[2,3]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[-3,2],[-3,5],[-1,6],[-1,1],[-3,2]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[2,5],[2,2],[8,2],[6,5],[2,5]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[1,0],[6,0],[6,3],[2,3],[1,0]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang

w.close() # Untuk menutup Writer