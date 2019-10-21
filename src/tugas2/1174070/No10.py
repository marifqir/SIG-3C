# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:29:39 2019

@author: User
"""

import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor10', shapeType=5) # Membuat penggambar pada shapefile yang nantinya akan di namakan nomor10 dan bentuknya itu adalah shapetype 5 yaitu Polygon

w.field("C1","C") # Membuat table dengan kolom pertama
w.field("C2","C") # Membuat table dengan kolom kedua
 
w.record("nama","saya")     #Mengisi table pada kolom satu yaitu nama dan kolom dua yaitu saya
w.record("adalah","sangat") #Mengisi table pada kolom satu yaitu adalah dan kolom dua yaitu sangat
w.record("panjang","dan")   #Mengisi table pada kolom satu yaitu panjang dan kolom dua yaitu dan 
w.record("sangat","ribet")  #Mengisi table pada kolom satu yaitu sangat dan kolom dua yaitu ribet
w.record("jadi","jangan")   #Mengisi table pada kolom satu yaitu jadi dan kolom dua yaitu jangan
w.record("diikuti","ya")    #Mengisi table pada kolom satu yaitu diikuti dan kolom dua yaitu ya

w.poly([[[1,1],[3,1],[3,3],[1,3],[1,1]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang 
w.poly([[[5,1],[7,1],[7,3],[5,3],[5,1]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[9,1],[11,1],[11,3],[9,3],[9,1]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[1,5],[3,5],[3,7],[1,7],[1,5]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[5,5],[7,5],[7,7],[5,7],[5,5]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[9,5],[11,5],[11,7],[9,7],[9,5]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang

w.close() # Menutup penggambar (writer) karena kita sudah beres menggambar yang kita perlukan