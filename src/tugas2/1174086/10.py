# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:31:16 2019

@author: acer
"""

import shapefile 
w=shapefile.Writer("soal10") 
w.shapeType 

w.field("kolom1","C") 
w.field("kolom2","C")



w.record("pororo","satu") 
w.record("kuy","dua")
w.record("wew","tiga")
w.record("lol","empat") 
w.record("top","lima")
w.record("dor","enam") 
w.record("hhh","tujuh")
w.record("iii","delapan")

 
w.poly([[[2,10],[12,10], [8,15],[5,15],[2,10]]]) 
w.poly([[[8,6],[18,6], [15,11],[11,11],[8,6]]]) 
w.poly([[[-2,-4],[8,-4], [5,1],[1,1],[-2,-4]]]) 
w.poly([[[18,20],[28,20], [25,25],[21,25],[18,20]]])  
w.poly([[[-8,-6],[-18,-6], [-15,-11],[-11,-11],[-8,-6]]])
w.poly([[[10,8],[20,8], [17,13],[13,13],[10,8]]]) 
w.poly([[[30,28],[40,28], [37,33],[33,33],[30,28]]]) 
w.poly([[[-30,-28],[-40,-28], [-37,-33],[-33,-33],[-30,-28]]]) 
 
w.close()