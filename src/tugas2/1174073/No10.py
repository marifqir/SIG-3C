# -*- coding: utf-8 -*-
"""
@author: Ainul Filiani
"""
import shapefile # Meng-import library shapefile
w = shapefile.Writer('Nomor10', shapeType=5) # Membuat penggambar pada shapefile yang nantinya akan di namakan nomor10 dan bentuknya itu adalah shapetype 5 yaitu Polygon

w.field("C1","C") # Membuat table dengan kolom pertama
w.field("C2","C") # Membuat table dengan kolom kedua
 
w.record("nama","ainul")     
w.record("d4ti3c","kelasku") 
w.record("alamat","aceh")   
w.record("semangat","belajar")
w.record("belajar","ranjin")
w.record("mantap","betul")  
w.record("mantap","ok")


w.poly([[[1,1],[2,1],[3,1],[4,3],[2,1]]])   
w.poly([[[9,8],[7,6],[1,8],[6,7],[9,2]]])  
w.poly([[[7,5],[7,6],[7,7],[7,8],[7,9]]]) 
w.poly([[[11,5],[12,5],[13,7],[14,7],[6,5]]])  
w.poly([[[8,9],[9,10],[10,7],[5,2],[8,8]]])   
w.poly([[[11,10],[11,11],[5,4],[8,4],[2,3]]]) 
w.poly([[[7,5],[7,6],[7,7],[7,8],[7,9]]]) 
w.close() 