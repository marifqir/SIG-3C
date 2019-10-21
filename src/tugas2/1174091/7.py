# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:57:03 2019

@author: User
"""

import shapefile #mengimport library shapefile
w=shapefile.Writer('nomor7',shapetype=5)#membuat shapefile dengan nama "nomor7" dengan shapetype 3 (polygon) 
w.shapeType 
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("ngek","satu") 
 
 
w.poly([[[1,3],[5,3],[1,2],[5,2]]]) 
 
w.close()