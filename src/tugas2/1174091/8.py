# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:01:42 2019

@author: User
"""

import shapefile #mengimport library shapefile
w=shapefile.Writer('nomor8',shapetype=5) #membuat shapefile dengan nama "nomor8" dengan shapetype 5 (polygon)
w.shapeType 
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("ngek","satu") 
 
 
w.poly([[[1,3],[5,3],[1,2],[5,2],[1,3]]]) 
 
w.close()