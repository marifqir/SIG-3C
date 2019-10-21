# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:49:40 2019

@author: acer
"""

import shapefile 
w=shapefile.Writer('soal6',shapeType=5)
w.shapeType 

w.field("kolom1","C")
w.field("kolom2","C")
 
w.record("ngek","satu") 
 
 
w.poly([[[1,3],[5,3]]]) 
w.close()

