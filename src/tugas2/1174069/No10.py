# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:24:30 2019

@author: FannyShafira
"""

import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor10', shapeType=5) # Membuat penggambar pada shapefile yang nantinya akan di namakan nomor10 dan bentuknya itu adalah shapetype 5 yaitu Polygon

w.field("C1","C") # Membuat table dengan kolom pertama
w.field("C2","C") # Membuat table dengan kolom kedua
 
w.record("Boyband","Korea")     #Mengisi table pada kolom satu yaitu boyband dan kolom dua yaitu korea
w.record("yang","saya") #Mengisi table pada kolom satu yaitu yang dan kolom dua yaitu saya
w.record("sukai","diantaranya")   #Mengisi table pada kolom satu yaitu sukai dan kolom dua yaitu diantaranya
w.record("adalah","EXO")  #Mengisi table pada kolom satu yaitu adalah dan kolom dua yaitu EXO
w.record("SEVENTEEN","SUPERJUNIOR")   #Mengisi table pada kolom satu yaitu SEVENTEEN dan kolom dua yaitu SUPERJUNIOR
w.record("WANNAONE","Dan masih banyak lagi")    #Mengisi table pada kolom satu yaitu WANNAONE dan kolom dua yaitu dan masih banyaklagi

w.poly([[[1,1],[3,1],[3,3],[1,3],[1,1]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang 
w.poly([[[5,1],[7,1],[7,3],[5,3],[5,1]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[9,1],[17,1],[17,3],[9,3],[9,1]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[2,9],[7,11],[7,16],[2,11],[2,9]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[5,10],[17,5],[17,7],[9,7],[11,5]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[9,5],[11,5],[11,7],[9,7],[9,5]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang

w.close() # Menutup penggambar (writer) karena kita sudah beres menggambar yang kita perlukan