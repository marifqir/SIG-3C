# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:04:32 2019

@author: User
"""

import shapefile #mengimport library shapefile
w=shapefile.Writer('nomor9',shapetype=5) #membuat shapefile dengan nama "nomor9" dengan shapetype 5 (polygon)
w.shapeType 
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("ngek","satu") 
w.record("crot","dua") 
 
 
 
w.poly([[[1,3],[5,3], [5,2],[1,2],[1,3]]]) 
w.poly([[[1,6],[5,6], [5,9],[1,9],[1,6]]]) 
 
 
w.save("soal9") 