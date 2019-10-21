# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:35:48 2019

@author: User
"""

 
import shapefile #mengimport library shapefile
w=shapefile.Writer('nomor4',shapefile.POINT) #membuat shapefile dengan nama "nomor4" dengan bentuk point
w.shapeType 
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("ngek","satu") 
w.record("ngok","dua") 
 
w.point(1,1) 
w.point(2,2) 
 
w.close()