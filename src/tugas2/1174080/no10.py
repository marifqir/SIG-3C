# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:44:42 2019

@author: HP
"""

import shapefile # Mengimportkan library shapefile
w = shapefile.Writer('no10', shapeType=5)  # Untuk fungsi writer yang digunakan untuk menggambar dan akan dinamakan no10 dalam bentuk shapetype=5 yang merupakan sebuah polygon
  
w.field("kolom1","C")  # untuk membuat kolom pertama pada table
w.field("kolom2","C")  # untuk membuat kolom dua pada table
 
w.record("semoga","keluarga") 
w.record("saya","sehat") 
w.record("sampai","nanti") 
w.record("membalas","nikmat") 
w.record("yang","telah") 
w.record("engkau","berikan")
w.record("membalas","nikmat") 
w.record("yang","telah") 
w.record("engkau","berikan")

w.poly([[[-4,0],[0,5],[4,0]]]) 
w.poly([[[-4,-2],[-1,2],[2,-2]]]) 
w.poly([[[-1,1],[2,6],[5,1]]])
w.poly([[[0,0],[4,5],[8,0]]])
w.poly([[[2,2],[4,6],[6,2]]]) 
w.poly([[[0,0],[4,5],[8,0]]]) 
w.poly([[[-4,0],[0,6],[4,0]]]) 
w.poly([[[-4,-2],[-1,3],[2,-2]]]) 
w.poly([[[-1,1],[2,7],[5,1]]])

w.close() # Menutup writer