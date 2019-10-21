# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:17:27 2019

@author: ADVENT
"""
import shapefile # Meng-import library shapefile
w = shapefile.Writer('10', shapeType=5) # untuk Membuat penggambar pada shapefile yang nantinya akan di namakan nomor10 dan bentuknya itu adalah shapetype 5 yaitu Polygon

w.field("C1","C") # untuk Membuat table dengan kolom pertama
w.field("C2","C") # untuk Membuat table dengan kolom kedua
 
w.record("alex","ferguso")     # untuk Mengisi table pada kolom satu yaitu nama dan kolom dua
w.record("gagak","guguk")        # untuk Mengisi table pada kolom satu yaitu nama dan kolom dua
w.record("bujang","kijang")    # untuk Mengisi table pada kolom satu yaitu nama dan kolom dua 
w.record("lama","ribet")   # untuk Mengisi table pada kolom satu yaitu nama dan kolom dua
w.record("tunggu","bosan")    # untuk Mengisi table pada kolom satu yaitu nama dan kolom dua
w.record("bucat","cabut")     # untuk Mengisi table pada kolom satu yaitu nama dan kolom dua
w.record("habis","cepat")     # untuk Mengisi table pada kolom satu yaitu nama dan kolom dua
w.record("malam","sendiri")     # untuk Mengisi table pada kolom satu yaitu nama dan kolom dua


w.poly([[[-4,-4],[-9,-10],[-12,-4],[-4,-4]]])   # untuk membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[-5,-5],[-11,-12],[-13,-5],[-5,-5]]])   # untuk membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[-6,-6],[-12,-13],[-14,-6],[-6,-6]]])   # untuk membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[-7,-7],[-13,-14],[-15,-7],[-7,-7]]])   # untuk membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[0,0],[4,5],[8,0],[0,0]]])   # untuk membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang 
w.poly([[[1,1],[5,6],[9,1],[1,1]]])   # untuk membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[2,2],[7,8],[10,2],[2,2]]])   # untuk membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang
w.poly([[[3,3],[8,9],[11,3],[3,3]]])   # untuk membuat garis dengan cara menghubungkan setiap titik yang digambar yang nantinya akan dihubungkan seluruh hingga membentuk suatu bidang


w.close() # untuk Menutup penggambar (writer) karena kita sudah beres menggambar yang kita perlukan