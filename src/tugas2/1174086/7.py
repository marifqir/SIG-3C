# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 20:53:08 2019

@author: acer
"""

import shapefile 
w=shapefile.Writer('soal7') 
w.shapeType 
w.field("kolom1","C") 
w.field("kolom2","C") 
w.record("ngek","satu") 
 
 
w.poly([[[1,3],[5,3],[1,2],[5,2]]]) 
w.close()