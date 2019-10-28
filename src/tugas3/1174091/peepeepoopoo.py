# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:06:31 2019

@author: User
"""

import shapefile #mengimport library shapefile
w=shapefile.Writer('nomor10',shapetype=5)#membuat file dengan nama "nomor10" dengan shapetype 5 (polygon")
w.shapeType 
 
w.field("kolom1","C") 
w.field("kolom2","C") 


w.record("POG","satu") 
w.record("CHAMP","dua") 
w.record("pepe","tiga")
w.record("gaga","empat")
w.record("omega","lima")
w.record("lulz","enam")
w.record("feels","tujuh")
w.record("good","delapan")
w.record("man","sembilan") 


w.poly([[[1,1],[3,1],[3,2],[1,2]]]) 
w.poly([[[4,1],[6,1],[6,2],[4,2]]]) 
w.poly([[[7,1],[9,1],[9,2],[7,2]]]) 
w.poly([[[10,1],[12,1],[12,2],[10,2]]]) 
w.poly([[[1,3],[3,3],[3,4],[1,4]]]) 
w.poly([[[4,3],[6,3],[6,4],[4,4]]]) 
w.poly([[[7,3],[9,3],[9,4],[7,4]]]) 
w.poly([[[10,3],[12,3],[12,4],[10,4]]])
w.poly([[[1,5],[3,5],[3,6],[1,6]]]) 
 
 
w.close()