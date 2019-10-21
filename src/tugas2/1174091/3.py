# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:16:20 2019

@author: User
"""

import shapefile #mengimport library shapefile
w=shapefile.Writer('nomor3',shapeType=3) #mengubah bentuk menjadi garis
w.shapeType 
w.shapeType=1 #mengubah dari garis yang di atas menjadi titik
w.shapeType 
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("ngek","satu") 
w.record("ngok","dua") 
 
w.point(1,1) 
w.point(2,2) 
 
w.close()