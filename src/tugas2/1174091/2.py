# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:36:48 2019

@author: User
"""

import shapefile #mengimport library shapefile
w=shapefile.Writer('nomor2', shapeType=1) #memberi nama shapefile "nomor2" dengan shapetype 1 (titik)
w.shapeType #melihat bentuk yang digunakan
 
w.field("kolom1","C") 
w.field("kolom2","C") 
 
w.record("ngek","satu") 
w.record("ngok","dua") 
 
w.point(1,1) 
w.point(2,2) 
 
w.close()