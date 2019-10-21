# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:09:21 2019

@author: PandA23
"""

import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor10', shapeType=5) # Membuat penggambar pada shapefile yang akan 
                                            #di namakan nomor10 dan bentuknya adalah shapetype 5 yaitu Polygon

w.field("A1","C") # Membuat table dengan kolom pertama
w.field("A2","C") # Membuat table dengan kolom kedua

w.record("satu","dua")     #Mengisi table pada kolom satu yaitu satu dan kolom dua yaitu dua
w.record("tiga","empat") #Mengisi table pada kolom satu yaitu tiga dan kolom dua yaitu empat
w.record("lima","enam")   #Mengisi table pada kolom satu yaitu lima dan kolom dua yaitu enam 
w.record("tujuh","delapan")  #Mengisi table pada kolom satu yaitu tujuh dan kolom dua yaitu delapan
w.record("sembilan","sepuluh")     #Mengisi table pada kolom satu yaitu sembilan dan kolom dua yaitu sepuluh
w.record("sebelas","duabelas") #Mengisi table pada kolom satu yaitu adalah sebelas kolom dua yaitu duabelas
w.record("tigabelas","empatbelas")   #Mengisi table pada kolom satu yaitu tigabelas dan kolom dua yaitu empatbelas 
w.record("limabelas","enambelas")  #Mengisi table pada kolom satu yaitu limabelas dan kolom dua yaitu enambelas


w.poly([[[-1,-1],[-3,-1],[-1,-4],[-1,-1]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang 
w.poly([[[-3,-1],[-5,-1],[-5,-4],[-3,-1]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[-5,-4],[-5,-7],[-3,-7],[-5,-4]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[-3,-7],[-1,-7],[-1,-4],[-3,-7]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[1,1],[3,1],[1,4],[1,1]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang 
w.poly([[[3,1],[5,1],[5,4],[3,1]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[5,4],[5,7],[3,7],[5,4]]]) #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[3,7],[1,7],[1,4],[3,7]]])   #membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang

w.close() # Menutup penggambar (writer) karena kita sudah selsai menggambar yang kita gambar