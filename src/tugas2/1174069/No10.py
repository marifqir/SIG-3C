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



w.poly([[[2,3],[4,6],[6,3],[4,0],[2,3]]]) # Membuat garis dengan menghubungkan titik-titik sehingga nantinya akan membentuk sebuah bidang
w.poly([[[-9,-2],[-2,-9],[5,-2],[-2,5],[-9,-2]]])
w.poly([[[-4,-1],[-1,-5],[2,-1],[-1,3],[-4,-1]]])
w.poly([[[-2,-1],[1,4],[4,1],[1,-2],[-2,-1]]])
w.poly([[[3,6],[7,3],[11,6],[7,9],[3,6]]])
w.poly([[[-1,-2],[2,-6],[5,-2],[2,3],[-1,-2]]])

w.close() # Menutup penggambar (writer) karena kita sudah beres menggambar yang kita perlukan