# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:48:24 2019

@author: User
"""

import shapefile #mengimport library shapefile
w=shapefile.Writer('nomor6',shapetype=5) #membuat shapefile dengan nama "nomor6" dengan shapetype 5 (polygon)
w.shapeType 
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("ngek","satu") 
 
 
w.poly([[[1,3],[5,3]]]) #menghubungkan garis dengan menghubungkan titik koordinat yang ditulis
 
w.close()