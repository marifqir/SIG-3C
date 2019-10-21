# -*- coding: utf-8 -*-
"""
@author: Dini Permata Putri
"""
import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor10', shapeType=5) # Membuat penggambar pada shapefile yang nantinya akan di namakan nomor10 dan bentuknya itu adalah shapetype 5 yaitu Polygon

w.field("C1","C") # Membuat table dengan kolom pertama
w.field("C2","C") # Membuat table dengan kolom kedua
 
w.record("nama","dini")     
w.record("d4ti3c","kelasku") 
w.record("alamat","palembang")   
w.record("semangat","belajar")
w.record("belajar","ranjin")




w.poly([[[9,8],[7,6],[1,8],[6,7],[9,2]]])   
w.poly([[[1,1],[2,1],[3,1],[4,3],[2,1]]])  
w.poly([[[7,4],[7,5],[7,6],[7,7],[7,8]]]) 
w.poly([[[12,5],[13,5],[14,7],[15,7],[7,5]]])  
w.poly([[[7,9],[8,10],[9,7],[6,2],[9,8]]])   


w.close() 